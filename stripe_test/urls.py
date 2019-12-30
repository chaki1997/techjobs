from django.urls import path
from stripe_test import views

app_name = 'stripe_test'

urlpatterns = [

    path('',views.StripeView.as_view(),name='stripe')
]