from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm, LoginForm
from django.views import View
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.views.generic import TemplateView
from django.contrib.auth import authenticate,login,logout
#from django.core.urlresolvers import reverse
from django.urls import reverse
from django.shortcuts import redirect
from .tokens import account_activation_token
from .models import CustomUser
from profile_wizard import models as profile_models

# Create your views here.

class RegisterView(View):
    form_class = RegistrationForm
    initial = {'key': 'value'}
    template_reg_end = 'users/done.html'
    template_name = 'users/sign_up.html'
    #template_name = 'users/login.html'
    email_exists_msg = 'This email is already in use.'

    def get(self,request):
        form = self.form_class(initial=self.initial)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        #print (form)
        #print(form.is_valid())
        print(form)
        if form.is_valid():
            data=form.cleaned_data
            print (data['status'])
            #if  (CustomUser.objects.filter(username=data['username']).exists() or CustomUser.objects.filter(email=data['email']).exists()):
            #    return render(request, self.template_name, {'form': form,"msg":self.email_exists_msg,})
            user = form.save(commit=False)

            #print(user.id)
            user.is_active = True
            user.status = data['status']
            user.save()

            subject = 'mail from django'
            current_site = get_current_site(request)


            message = render_to_string('activate/acc_active_email.html', {
                'user':user,
                'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })

            mail_from =  settings.EMAIL_HOST_USER
            #mail_to = 'gio.sanikidze@gmail.com'
            mail_to = 'no-reply@techjobs.awsapps.com'
            send_mail(subject,
                       message,
                       mail_from,
                       [mail_to],
                       fail_silently = False)

            return render(request, self.template_reg_end, {'form': form})
        return render(request, self.template_name, {'form': form})


class Activate(View):

    def get(self,request, uidb64, token,*args, **kwargs):

        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None
        #print(user.id)
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
        #login(request, user)
        # return redirect('home')
            return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        else:
            return HttpResponse('Activation link is invalid!')


class LoginView(TemplateView):

    initial = {'key': 'value'}
    initial = {'key': 'value'}
    form_class    = LoginForm
    template_name = 'users/index.html'
    template_log = 'home/home_log.html'

    def get(self,request):
        login_form = self.form_class(initial=self.initial)
        return render(request,self.template_name,{'login_form':login_form})

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        print (form)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=str(data['username']),password=str(data['password1']))

            if user is not None:
                print (user)
                login(request, user)
                print(request.user.id)
                print(request.user.status)
                user = CustomUser.objects.get(pk=request.user.id)
                #print (user.is_employer == True)
                print (user.status)
                if user.status == 'Employer':
                #return redirect(reverse('profiles_test:profiles'))
                    #return redirect(reverse('profile_wizard:profile_wizard'))
                    return redirect(reverse('home:index'))
                elif user.status == 'Job Seeker':
                    jobseeker = profile_models.EmployeeProfileModel.objects.filter(user=request.user)
                    if jobseeker:
                        return redirect(reverse('home:index'))
                    else:
                        return redirect(reverse('profile_wizard:profile_wizard' ,kwargs={'step': 'starter'}))

                    #return redirect(reverse('profile_wizard:job_post_wizard'))
                    #return redirect('/profile/client/index')


            else:
                msg='Username or Password is incorrenct'
                login_form = self.form_class(initial=self.initial)
                return render(request,self.template_name,{'login_form':login_form,'msg':msg})
        else:
            print('data is not valide')


class LogOut(TemplateView):
    template_name = 'home\home.html'
    def post(self, request):
        #print request.session['token']
        print ('logout')
        logout(request)

        return redirect(reverse('home:index'))


import json
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def adjaxresponse(request):
    if request.method == "POST" and request.is_ajax(): #os request.GET()
        get_value= request.POST
        # Do your logic here coz you got data in `get_value`
        data = {}
        data['result'] = True
        print('ajdax response')
        print(list(get_value.keys())[0])
        credential = list(get_value.keys())[0]
        if  CustomUser.objects.filter(username=credential).exists():
            #.exists() or CustomUser.objects.filter(email=data['email']).
            data['result'] = False
            return HttpResponse(json.dumps(data), content_type="application/json")
            #return HttpResponse(data, content_type="application/json")

        else:

            return HttpResponse(json.dumps(data), content_type="application/json")