from django.shortcuts import render
from django.shortcuts import get_object_or_404
import os
from django.conf import settings
from django.shortcuts import render,render_to_response
from django.views.generic import TemplateView,ListView,DetailView
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect
import logging
from django.contrib.auth import update_session_auth_hash
from users import forms
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

from django.contrib import messages
from jobapply.models import JobApply
from django.views.generic.edit import FormView,UpdateView

# Create your views here.

class MessagesViews(TemplateView):
    template_name = 'messages/index.html'
    def get(self,request,**kwargs):
        return render(request,self.template_name,{})

    def post(self,request,**kwargs):
        return render(request,self.template_name,{})
