from django.urls import path
from . import views



app_name = 'paypal_subscription'


urlpatterns = [

    #path('',views.ProfileFormWizardView.as_view([ProfileForm1,ProfileForm2,ProfileForm3]),name='profiles_wizard'),


    path('<int:plan_id>/<slug:plan_slug>/',
        views.SubscriptionView.as_view(), name='subscription_detail'),
    path('payment-done/', views.payment_done, name='done'),
    path('payment-cancelled/', views.payment_canceled, name='canceled'),
    path('payout',views.ContractAdmin.as_view(),name='contracts'),
    path('payout/<pk>',views.ContractsPayOut.as_view(),name='payouts'),






]