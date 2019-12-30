from django.contrib import admin

# Register your models here.

from .models import JobApply,Contract

admin.site.register(JobApply)
admin.site.register(Contract)

