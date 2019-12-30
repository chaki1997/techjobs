import os
from django.conf import settings
from django.shortcuts import render,render_to_response
from django.views.generic import TemplateView,ListView,DetailView
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect
import logging
from django.contrib.auth import update_session_auth_hash
#from users import forms
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from .formset_employee import EducationFormSet,EmploymentFormSet
from django.db import transaction

from django.urls import reverse_lazy
from .models import EmployeeProfileModel,\
                    EducationWizard,\
                    EduWizard,\
                    EmloymentWizard


from django.views.generic.edit import FormView,UpdateView
'''
class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)
'''

class ProfileStepUpdate(UpdateView):
    model = EmployeeProfileModel
    success_url = '/'
    fields = ['first_name', 'last_name']
class ProfileUpdate(UpdateView):
    model = EmployeeProfileModel
    fields = ['status','prof_title','prof_overview','language_compatancy',
              'payment','category_industry','availability',
               'address_1','address_2','city','zip_code','country','phone']

    template_name = 'profiles/employee/update.html'
    success_url = reverse_lazy('profile_wizard:settings')

    def get_context_data(self, **kwargs):
        data = super(ProfileUpdate, self).get_context_data(**kwargs)
        #print(self.request)
        #print(self.kwargs)
        if self.request.POST:
            data['education'] = EducationFormSet(self.request.POST, instance=self.object)
            data['employment'] = EmploymentFormSet(self.request.POST,instance=self.object)
            #print(data['employment'])
        else:
            data['education'] = EducationFormSet(instance=self.object)
            data['employment'] = EmploymentFormSet(instance=self.object)
            #print(data)
            #print(data['employment'])
            education = EduWizard.objects.filter(profile=data['object'])
            employment = EmloymentWizard.objects.filter(profile=data['object'])
            data['edudata'] = education
            data['empdata'] = employment
            #print(self.object)
            paralel_edu = zip( data['education'],data['edudata'])
            paralel_emp = zip(data['employment'],data['empdata'])
            data['paralel'] = paralel_edu
            data['paralel_emp'] = paralel_emp
        return data
    def form_invalid(self,form):
        print('form_is invalid')
        return super(ProfileUpdate, self).form_invalid(form)


    def form_valid(self, form):
        context = self.get_context_data()
        education = context['education']
        employment = context['employment']
        print('test1')
        with transaction.atomic():
            self.object = form.save()
            print('test2')
            if education.is_valid() and employment.is_valid():
                #
                print('edu is valide')
                education.instance = self.object
                education.save()
                employment.instance = self.object
                employment.save()
            else:
                print(employment)
        return super(ProfileUpdate, self).form_valid(form)