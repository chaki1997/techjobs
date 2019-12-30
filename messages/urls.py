from django.urls import path
from profile_wizard import views,views_employee
from .views import MessagesViews

app_name = 'messages'



urlpatterns = [



    path('<slug>', MessagesViews.as_view(), name='job_post_wizard'),

]