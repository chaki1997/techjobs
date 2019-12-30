from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [



    #path('index',views.Index.as_view(),name='index'),
    path('',views.Index.as_view(),name='index'),
    #path('',views.ComingSoon.as_view(),name='index'),
    #path('signed',views.HomeLog.as_view(),name='homelog'),
    path('about',views.About.as_view(),name='about'),
    #path('',views.ComingSoon.as_view(),name='about')
    path('terms',views.TermsView.as_view(),name='terms'),
    path('privacy',views.PrivacyView.as_view(),name='privacy'),
    path('contact',views.Contact.as_view(),name='contact'),
    path('contest',views.Contest.as_view(),name='contest'),
]