from django.contrib import admin

# Register your models here.

from .models import SubscriptionPlan,Subscribtion

admin.site.register(SubscriptionPlan)
admin.site.register(Subscribtion)
