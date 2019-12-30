from django.urls import path
from . import views



app_name = 'jobapply'


urlpatterns = [




    #path('<int:plan_id>/<slug:plan_slug>/',
    #    views.SubscriptionView.as_view(), name='subscription_detail'),
    path('<int:id>', views.ApplyToJob.as_view(), name='applyform'),
    path('myemp/<pk>',views.MyEmployee.as_view(),name='myemployee'),
    path('contract/<id>',views.ContractPay.as_view(),name='contract'),
    path('mycontracts/<slug>',views.Mycontracts.as_view(),name='mycontracts'),
    path('mycontracts/<slug>/<pk>',views.Mycontracts.as_view(),name='mycontracts'),
    path('payment-done/', views.payment_done, name='done'),
    path('payment-cancelled/', views.payment_canceled, name='canceled'),






]