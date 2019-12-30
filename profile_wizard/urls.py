from django.urls import path
from profile_wizard import views,views_employee
from .forms import ProfileForm1,ProfileForm3
from .views import FORMS,ajax_post,JOBPOSTFORMS

app_name = 'profile_wizard'


jobpost = views.JobPostWizardWiew.as_view(JOBPOSTFORMS,
    url_name='profile_wizard:job_post_wizard', done_step_name='finished')

employer = views.ProfileFormWizardView.as_view(FORMS,
    url_name='profile_wizard:profile_wizard',done_step_name='done')

urlpatterns = [

    #path('',views.ProfileFormWizardView.as_view([ProfileForm1,ProfileForm2,ProfileForm3]),name='profiles_wizard'),

    path('client/<step>', jobpost, name='job_post_wizard'),
    path('postjob',views.PostJobView.as_view(),name='postjob'),
    path('freelancer/<step>',employer,name='profile_wizard'),
    #path('listview',views.FreelancerListView.as_view(),name='freelancer_list'),
    path('slug/<slug>', views.FreelancerListPagView.as_view(), name='freelancer_list'),
    #path('<slug>', views.FreelancerListPagView.as_view(), name='freelancer_list'),
    path('joblist/<slug>/',views.JobListView.as_view(),name='joblist'),
    path('jobdetail/<id>/',views.JobDetailView.as_view(),name='job-detail'),
    path('post',views.ajax_post,name='form_step_edu'),
    path('detail/<id>/', views.FreelancerDetailView.as_view(), name="profile-detail"),
    path('search',views.SearchResultsView.as_view(),name='search'),

    #Img uploading testing
    path('test',views.ProfileTest.as_view(),name='test'),
    path('test/detile',views.ProfileTestDetile.as_view(),name='detile'),


    path('settings/',views.SettingsView.as_view(),name='settings'),
    path('settings/password',views.UserPassChange.as_view(),name='password'),
    path('settings/employer/<pk>',views.EmployerProfileReview.as_view(),name='employer_review'),
    path('settings/employer',views.CompanyCreate.as_view(),name='company_create'),
    path('settings/myjobs',views.MyJobs.as_view(),name='myjobs'),

    #path('settings/employee',views.EmployeeReview.as_view(),name='employee'),
    path('settings/update/<pk>',views_employee.ProfileUpdate.as_view(),name='update'),





]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
