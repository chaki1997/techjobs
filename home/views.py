from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView
from users import forms
from django.conf import settings
from paypal_subscription.models import SubscriptionPlan
from jobapply import models
from django.contrib import messages
from profile_wizard import models as employee
# Create your views here.
class Index(TemplateView):
    initial = {'key': 'value'}
    template_name = 'home/home.html'

    template_name_looged = 'home/home_log.html'
    form_register = forms.RegistrationForm
    form_login = forms.LoginForm

    def get(self,request):
        print(settings.STATIC_ROOT)
        form_r = self.form_register(initial=self.initial)
        form_l = self.form_login(initial=self.initial)
        userData = {}
        context = {}
        if request.user.is_authenticated:
            #print ('user is logged')
            print(request.user.is_superuser)
            context['user']=request.user
            print(context['user'].status)
            subscription_plan = SubscriptionPlan.objects.all()
            context['subscription_plan'] = subscription_plan
            object = models.JobApply.objects.filter(jobowner=request.user)
            #print(object)



            if object:
                #print('object is not empty')
                messages.success(request, 'Someone applied to the vacany')
                #print(messages)
            #print (context['subscription_plan'])

            return render(request,self.template_name_looged,context)
        else:
            #print ('user in not logged')
            print('.......')
        return render(request,self.template_name,{'form_r':form_r,'form_l':form_l})


class About(TemplateView):
    initial = {'key': 'value'}
    template_name = 'home/about.html'
    template_name_looged = 'home/about_log.html'
    form_register = forms.RegistrationForm
    form_login = forms.LoginForm
    def get(self,request):
        if request.user.is_authenticated:
            return render(request, self.template_name_looged)
        return render(request, self.template_name)

class ComingSoon(TemplateView):
    initial = {'key': 'value'}
    template_name = 'home/comingsoon.html'


    def get(self,request):
        return render(request, self.template_name)



class HomeLog(TemplateView):
    initial = {'key': 'value'}
    template_name = 'home/home_log.html'

    def get(self,request):
        print('homelog')
        print (request.user.first_name)
        context = {}
        context['id']=request.user
        return render(request,self.template_name,context)

class TermsView(TemplateView):
    template_name_log = 'terms_privacy/terms_log.html'
    template_name = 'terms_privacy/terms.html'

    def get(self,request):
        if request.user.is_authenticated:
            return render(request, self.template_name_log)
        return render(request, self.template_name)

class PrivacyView(TemplateView):
    template_name_log = 'terms_privacy/privacy_log.html'
    template_name = 'terms_privacy/privacy.html'
    form_class = forms.RegistrationForm

    def get(self,request):

        if request.user.is_authenticated:
            return render(request, self.template_name_log)
        return render(request, self.template_name)


class Contact(TemplateView):
    template_name = 'home/contact/contact.html'
    template_name_log = 'home/contact/contact_log.html'
    def get(self,request):
        if request.user.is_authenticated:
            return render(request,self.template_name_log)
        return render(request,self.template_name)

class Contest(TemplateView):
    template_name = 'home/contest/contest.html'
    template_name_log = 'home/contest/contest_log.html'
    def get(self,request):
        if request.user.is_authenticated:
            return render(request,self.template_name_log)
        return render(request,self.template_name)
