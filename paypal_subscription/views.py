
from django.shortcuts import render, HttpResponse, redirect, \
    get_object_or_404, reverse

from django.views.generic import TemplateView
from .models import SubscriptionPlan
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from jobapply import models as contracts



# Create your views here.

class SubscriptionView(TemplateView):

    template_name ='paypal_subscription/subscription_detail.html'
    context = {}



    def get(self,request,plan_id,plan_slug):
        #host = request.get_host()
        host = '4e7f5645.ngrok.io'
        plan = get_object_or_404(SubscriptionPlan,id=plan_id)

        print(request.user.id)
        self.context['object'] = plan
        paypal_dict = {
            "cmd": "_xclick-subscriptions",
            'business': settings.PAYPAL_RECEIVER_EMAIL,
             "a3": plan.price,  # monthly price
             "p3": plan.billing_cycle,  # duration of each unit (depends on unit)
             "t3": plan.billing_cycle_unit,  # duration unit ("M for Month")
            "src": "1",  # make payments recur
            "sra": "1",  # reattempt payment on payment error
            "no_note": "1",  # remove extra notes (optional)
            'item_name': plan.name,
            'custom': request.user.id,  # custom data, pass something meaningful here
            'currency_code': 'USD',
            'notify_url': 'http://{}{}'.format(host,
                                               reverse('paypal-ipn')),
            'return_url': 'http://{}{}'.format(host,
                                               reverse('paypal_subscription:done')),
            'cancel_return': 'http://{}{}'.format(host,
                                                  reverse('paypal_subscription:canceled')),
        }
        form = PayPalPaymentsForm(initial=paypal_dict, button_type="subscribe")
        self.context['form']=form
        return render(request,self.template_name,self.context)

def payment_done(request):
    return render(request, 'paypal_subscription/payment_done.html')

@csrf_exempt
def payment_canceled(request):
    return render(request, 'paypal_subscription/payment_cancelled.html')

class ContractAdmin(TemplateView):
    template_name = 'paypal_subscription/contracts_payout.html'
    def get(self,request,**kwargs):
        queryset = contracts.Contract.objects.all()
        return render(request,self.template_name,{'objs':queryset})


class ContractsPayOut(TemplateView):
    template_name = 'paypal_subscription/paypal_payout.html'
    context = {}

    def get(self, request, **kwargs):
        # host = request.get_host()
        host = '8a1731e1.ngrok.io'
        contract = get_object_or_404(contracts.Contract, id=kwargs['pk'])

        print(request.user.email)

        self.context['object'] = contract
        amount = contract.job_signed.budjet
        print(amount)
        print(contract.employee.email)
        paypal_dict = {
            'business': contract.employee.email,
            'amount': amount,
            'item_name': 'Order {}'.format(contract.id),
            'invoice': str(contract.id),
            'custom': 'payout',  # custom data, pass something meaningful here
            'currency_code': 'USD',
            'notify_url': 'http://{}{}'.format(host,
                                               reverse('paypal-ipn')),
            'return_url': 'http://{}{}'.format(host,
                                               reverse('paypal_subscription:done')),
            'cancel_return': 'http://{}{}'.format(host,
                                                  reverse('paypal_subscription:canceled')),
        }
        form = PayPalPaymentsForm(initial=paypal_dict)
        self.context['form'] = form
        self.context['amount'] = amount
        self.context['reciver'] = contract.employee
        return render(request, self.template_name, self.context)



