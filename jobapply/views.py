from django.shortcuts import render

# Create your views here.
from .forms import JobAbblyForm
from .models import JobApply,Contract
from profile_wizard import models as jobmodels
from django.shortcuts import render, HttpResponse, redirect, \
    get_object_or_404, reverse
from django.core.mail import send_mail
from django.views.generic import TemplateView
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from profile_wizard import models as profilemodels

class ApplyToJob(TemplateView):
    template_name = 'applytojob/applyform.html'
    templaye_applied = 'applytojob/done.html'
    form_class = JobAbblyForm
    initial = {'key':'value'}
    model = JobApply
    def get(self,request,**kwargs):
        form = self.form_class(initial=self.initial)
        print(kwargs)
        id = kwargs['id']
        print (id)
        user = request.user
        jobpost = jobmodels.PostJob.objects.get(id=id)

        applier_profile = jobmodels.EmployeeProfileModel.objects.get(user=request.user)
        print(applier_profile)
        print(type(jobpost.user))
        print(type(user))
        applier = user
        jobowner = jobpost.user
        job = jobpost
        coverletter = ''

        return render(request,self.template_name,{'form':form,'id':id})
    def post(self,request,**kwargs):
        form = self.form_class(request.POST)
        id = kwargs['id']
        print(id)
        user = request.user
        jobpost = jobmodels.PostJob.objects.get(id=id)
        print(type(jobpost.user))
        print(type(user))
        applier = user
        applier_profile = jobmodels.EmployeeProfileModel.objects.get(user=request.user)
        jobowner = jobpost.user
        job = jobpost
        coverletter = ''

        if form.is_valid():
            coverletter = form['coverletter']
            object = JobApply(applier = applier,
                              applier_profile =applier_profile,
                              jobowner = jobowner,
                              job = job,
                              coverletter = coverletter)
            object.save()
            subject = 'techjobs.one notification'
            message = 'someone applied to your job'
            mail_from = settings.EMAIL_HOST_USER
            mail_to = 'gio.sanikidze@gmail.com'
            send_mail(subject,
                      message,
                      mail_from,
                      [mail_to],
                      fail_silently=True)

            return redirect('profile_wizard:job-detail', kwargs['id'])


        return render(request,self.templaye_applied,{})

class MyEmployee(TemplateView):
    template_name = 'applytojob/employers.html'
    def get(self,request,**kwargs):
        user = request.user
        print(kwargs['pk'])
        job=profilemodels.PostJob.objects.get(id=kwargs['pk'])
        print(job)
        queryset = JobApply.objects.filter(jobowner = user,job=kwargs['pk'])
        print(queryset)
        #print(queryset[0].job)
        #print(queryset[0].applier)
        #print(queryset[0].jobowner)
        #print(queryset[0].job)
        return render(request,self.template_name,{'objects':queryset})

from paypal.standard.forms import PayPalPaymentsForm
class ContractPay(TemplateView):
    #order_id = request.session.get('order_id')
    #order = get_object_or_404(Order, id=order_id)
    # host = request.get_host()
    host = '8a1731e1.ngrok.io'
    #print('order {}'.format(order.total_cost))
    #print('host {}'.format(host))
    template_name = 'paypal_subscription/contract.html'

    def get(self,request,**kwargs):

        print(kwargs)
        order = get_object_or_404(JobApply, id=kwargs['id'])
        print(order.id)
        amount = order.job.budjet
        #return render(self.request, self.template_name)

        paypal_dict = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'amount': amount,
            'item_name': 'Order {}'.format(order.id),
            'invoice': str(order.id),
            'custom': 'pay_contract',
            'currency_code': 'USD',
            'notify_url': 'http://{}{}'.format(self.host,
                                           reverse('paypal-ipn')),
            'return_url': 'http://{}{}'.format(self.host,
                                           reverse('jobapply:done')),
            'cancel_return': 'http://{}{}'.format(self.host,
                                              reverse('jobapply:canceled')),
        }

        form = PayPalPaymentsForm(initial=paypal_dict)
        return render(request, self.template_name, {'order': order, 'form': form})
        #return render(request, self.template_name)


def payment_done(request):
    return render(request, 'paypal_subscription/payment_done.html')

@csrf_exempt
def payment_canceled(request):
    return render(request, 'paypal_subscription/payment_cancelled.html')


class Mycontracts(TemplateView):
    template_name = 'applytojob/contracts.html'
    model = Contract

    def get(self,request,**kwargs):
        print(kwargs)
        contract = []
        done_contracts = []
        if kwargs['slug'] == 'er':
            contract = Contract.objects.filter(employer=request.user).filter(status__in=['freelancer done','in progress'])
            done = Q(status__contains="done")
            paid = Q(status__contains="paid")
            #done_contracts = Contract.objects.filter(employee=request.user).filter(done | paid)
            done_contracts = Contract.objects.filter(employer=request.user).filter(status__in=['paid','done'])
            #done_contracts = Contract.objects.filter(employer=request.user, status='done')

            print(done_contracts)
            #Q(status__contains='done')
            return render(request,self.template_name,{'objs':contract,'done':done_contracts})
        if kwargs['slug'] == 'ee':
            contract = Contract.objects.filter(employee=request.user,status='in progress')

            done = Q(status__contains="done")
            paid  = Q(status__contains="paid")

            done_contracts = Contract.objects.filter(employee=request.user).filter(done | paid)

            print(done_contracts)
        return render(request, self.template_name, {'objs': contract, 'done': done_contracts})

    def post(self,request,**kwargs):
        print(kwargs)
        if kwargs['slug'] == 'er':
            contract = Contract.objects.get(id=kwargs['pk'])
            contract.status = 'done'
            contract.save()
            queryset = Contract.objects.filter(employer=request.user, status='in progress')
            #done_contracts = Contract.objects.filter(employer=request.user).filter(Q(status__contains='done'))
            done = Q(status__contains="done")
            paid = Q(status__contains="paid")

            done_contracts = Contract.objects.filter(employer=request.user).filter(done | paid)
            #return render(request, self.template_name, {'objs': queryset, 'done': done_contracts})
        if kwargs['slug'] == 'ee':
            print(kwargs)
            contract = Contract.objects.get(id=kwargs['pk'])
            contract.status = 'freelancer done'
            contract.save()
            done = Q(status__contains="done")
            print(contract.status)
            queryset = Contract.objects.filter(employer=request.user, status='in progress')
            #done_contracts = Contract.objects.filter(employee=request.user).filter(done)
            done = Q(status__contains="done")
            paid = Q(status__contains="paid")

            done_contracts = Contract.objects.filter(employee=request.user).filter(done | paid)
            print(done_contracts)
        return render(request, self.template_name, {'objs': queryset,'done':done_contracts})