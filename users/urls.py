from django.urls import path, re_path
from django.conf.urls import url
from django.contrib.auth.views import logout
from django.conf import settings
from users import views
from home import views as homeWievs
LOGOUT_REDIRECT_URL = 'main/index'
app_name = 'users'
#app_name = MyappConfig.name
urlpatterns = [

    path('signup/',views.RegisterView.as_view(),name='register'),
    path('login/', views.LoginView.as_view(),name='login'),
    path('get/', views.adjaxresponse,name='validate'),

    #logout
    path('main/index',homeWievs.Index.as_view(),name='index'),


    #path('logout/',views.LogOut.as_view(),name='logout'),
    path('logout',logout, {'next_page': LOGOUT_REDIRECT_URL},name='logout'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.Activate.as_view(), name='activate'),
]

