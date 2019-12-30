# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from profile_wizard import models
from django.contrib.auth.models import User

from .forms import RegistrationForm
from .models import CustomUser


class MyCustomUserInline(admin.StackedInline):
    model = models.FreeProfileWizard
    can_delete = True
    verbose_name = models.FreeProfileWizard



class CustomUserAdmin(UserAdmin):
    add_form = RegistrationForm
    inlines = (MyCustomUserInline, )

    model = CustomUser
    list_display = ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)
#admin.site.unregister(CustomUser)
#admin.site.register(CustomUser, UserAdmin)







