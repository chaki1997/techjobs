from paypal.standard.ipn.signals import valid_ipn_received,invalid_ipn_received
from django.dispatch import receiver
from paypal.standard.models import ST_PP_COMPLETED
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from datetime import datetime
from users import models
from .models import Subscribtion,SubscriptionPlan
from jobapply import models as apply

from django.shortcuts import get_object_or_404


@receiver(valid_ipn_received)
def ipn_receiver(sender, **kwargs):
    ipn_obj = sender

    # check for Buy Now IPN
    if ipn_obj.txn_type == 'web_accept':
        print('1.0!')
        if ipn_obj.payment_status == ST_PP_COMPLETED:
            # payment was successful
            print('1.1!')
            if ipn_obj.custom == 'pay_contract':

                applyjob = get_object_or_404(apply.JobApply, id=ipn_obj.invoice)
                print(apply)
                applyjob.status = 'signed'
                applyjob.save()
                obj = apply.Contract(status='in progress',
                                 job_signed = applyjob.job,
                                 employee=applyjob.applier,
                                 employer=applyjob.jobowner,
                                 jobapply=applyjob)
                obj.save()
            if ipn_obj.custom == 'payout':
                contract = get_object_or_404(apply.Contract,id=ipn_obj.invoice)
                contract.status = 'paid'
                contract.save()
                print('contract is paied')





    # check for subscription signup IPN
    elif ipn_obj.txn_type == "subscr_signup":
        print('2.0!')
        # get user id and activate the account
        id = ipn_obj.custom
        user = models.CustomUser.objects.get(id=id)
        plan = ipn_obj.item_name
        palan_obj = SubscriptionPlan.objects.get(name = plan)
        object = Subscribtion(user = user,plan = palan_obj)
        object.save()
        #user.active = True
        #user.save()

        #subject = 'Sign Up Complete'

        #message = 'Thanks for signing up!'

        #email = EmailMessage(subject,
        #                     message,
        #                     'admin@myshop.com',
        #                     [user.email])

        #email.send()

    # check for subscription payment IPN
    elif ipn_obj.txn_type == "subscr_payment":
        print('3.0!')
        # get user id and extend the subscription
        id = ipn_obj.custom
        print (ipn_obj.item_name)
        #user = User.objects.get(id=id)
        # user.extend()  # extend the subscription

        #subject = 'Your Invoice for {} is available'.format(
        #    datetime.strftime(datetime.now(), "%b %Y"))

        #message = 'Thanks for using our service. The balance was automatically ' \
         #         'charged to your credit card.'

        #email = EmailMessage(subject,
        #                     message,
        #                     'admin@myshop.com',
        #                     [user.email])

        #email.send()

    # check for failed subscription payment IPN
    elif ipn_obj.txn_type == "subscr_failed":
        pass
        print('4.0!')

    # check for subscription cancellation IPN
    elif ipn_obj.txn_type == "subscr_cancel":
        pass
        print('5.0!')


@receiver(invalid_ipn_received)
def ipn_invalid_receiver(sender,**kwargs):
    ipn_obj = sender
    print(ipn_obj)
    print('invalid')


