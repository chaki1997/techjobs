from django.shortcuts import get_object_or_404
import os
from django.conf import settings
from django.shortcuts import render,render_to_response
from django.views.generic import TemplateView,ListView,DetailView
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect
import logging
from django.contrib.auth import update_session_auth_hash
from users import forms
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from .moderation import moderation,job_moderation
from django.contrib import messages
from jobapply.models import JobApply
from django.views.generic.edit import FormView,UpdateView

from .models import FreeProfileWizard,\
                    EducationWizard,\
                    EduWizard,\
                    EmloymentWizard,\
                    Company,\
                    EmployeeProfileModel

# form imports
from .forms import ProfileForm1,\
                   ProfileForm3,\
                   EmplymentFormWizard,\
                   ProficiencyWizardForm,\
                   LocationWizardForm,\
                   EducationWizardForm,\
                    ReviewWizardForm
logr = logging.getLogger(__name__)

from formtools.wizard.views import SessionWizardView,NamedUrlSessionWizardView
# Create your views here.


class ProfileFormView(TemplateView):
    initial = {'key': 'value'}
    template_name = 'profiles/wizard/company_wizard.html'
    #form_class = ProfileForm
    #education_form = EducationForm

    def get(self,request):
        return render(request,self.template_name,{})



degree_list = ('Mexico', 'USA', 'China', 'France')

FORMS = [('starter', ProfileForm1),
        ('education', EducationWizardForm),
        ('first_education', EducationWizardForm),
         ('second_education', EducationWizardForm),
         ('employment',EmplymentFormWizard),
         ('first_employment',EmplymentFormWizard),
         ('second_employment',EmplymentFormWizard),
         #('hour_rate',ProfileForm3),
        ('proficiency',ProficiencyWizardForm),
        ('location',LocationWizardForm),
        ('review',ReviewWizardForm),



        ]

TEMPLATES = {
            'starter':'profiles/freelancer_wizard/starter.html',

             'education':'profiles/freelancer_wizard/education.html',
             'first_education':'profiles/freelancer_wizard/education.html',
             'second_education':'profiles/freelancer_wizard/education.html',

             'employment':'profiles/freelancer_wizard/Employment.html',
             'first_employment':'profiles/freelancer_wizard/Employment.html',
             'second_employment':'profiles/freelancer_wizard/Employment.html',
             #'hour_rate':'profiles/freelancer_wizard/hour_rate.html',
             'proficiency':'profiles/freelancer_wizard/proficiency.html',
             'location':'profiles/freelancer_wizard/location.html',
             'review':'profiles/freelancer_wizard/education_answers.html'


             }



from .form_wizard_dict import sort_forms_data


def employment_repeat_wizard_first(wizard):
    """Return true if user opts to pay by credit card"""
    # Get cleaned data from payment step
    # get employment step repeet first time
    cleaned_data = wizard.get_cleaned_data_for_step('employment') or {'repeat':False}
    # Return true if the user selected credit card
    #print(cleaned_data['repeat'])
    if cleaned_data['repeat'] == True:
        #print (cleaned_data['repeat'])
        return True
    else:
        return False
def employment_repeat_wizard_second(wizard):
    """Return true if user opts to pay by credit card"""
    # Get cleaned data from payment step
    # get employment step repeet first time
    cleaned_data = wizard.get_cleaned_data_for_step('first_employment') or {'repeat':False}
    # Return true if the user selected credit card
    #print(cleaned_data['repeat'])
    if cleaned_data['repeat'] == True:
        #print (cleaned_data['repeat'])
        return True
    else:
        return False
    # get employment step repeet second time
def education_repeat_wizard_first(wizard):
    """Return true if user opts to pay by credit card"""
    # Get cleaned data from payment step
    # get employment step repeet first time
    cleaned_data = wizard.get_cleaned_data_for_step('education') or {'repeat':False}
    # Return true if the user selected credit card
    #print(cleaned_data['repeat'])
    if cleaned_data['repeat'] == True:
        #print (cleaned_data['repeat'])
        return True
    else:
        return False
def education_repeat_wizard_second(wizard):
    """Return true if user opts to pay by credit card"""
    # Get cleaned data from payment step
    # get employment step repeet first time
    cleaned_data = wizard.get_cleaned_data_for_step('first_education') or {'repeat':False}
    # Return true if the user selected credit card
    #print(cleaned_data['repeat'])
    if cleaned_data['repeat'] == True:
        #print (cleaned_data['repeat'])
        return True
    else:
        return False
'''
def hour_rate_full_time_false(wizard):
    """Return true if user opts to pay by credit card"""
    # Get cleaned data from payment step
    # get employment step repeet first time
    cleaned_data = wizard.get_cleaned_data_for_step('starter') or {'status':False}
    # Return true if the user selected credit card
    #print(cleaned_data['repeat'])
    if cleaned_data['status'] == 'Freelancer':
        return True
    elif cleaned_data['status'] == 'Fulltime':
        return False
    elif cleaned_data['status'] == False:
        return False
'''
from django.utils.decorators import method_decorator
from django.core.files.storage import DefaultStorage
@method_decorator(login_required, name='dispatch')
class ProfileFormWizardView(SessionWizardView,NamedUrlSessionWizardView):
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT,'phostos'))
    #file_storage = DefaultStorage()

    image_name = {}

    condition_dict = {'first_employment': employment_repeat_wizard_first,
                      'second_employment': employment_repeat_wizard_second,
                      'first_education':education_repeat_wizard_first,
                      'second_education':education_repeat_wizard_second,
                     # 'hour_rate':hour_rate_full_time_false,
                      }

    #template_name = 'profiles/wizard/general.html'
    #form_list = [ProfileForm1,
    #             EducationWizardForm,
    #             #EmplymentFormWizard,
    #             ProfileForm3,
    #             #ProficiencyWizardForm,
    #             #LocationWizardForm
    # ]
    step_context_dict = {}
    data_session_key = "wizard_data"
    #form_class = ProfileForm2
    prefix_list = []
    data_list=[]
    data_dict = {}
    '''
    def get_context_data(self, **kwargs):
        context = super(ProfileFormWizardView, self).get_context_data(**kwargs)
        #context['all_data'] = self.get_all_cleaned_data()
        context['all_data'].update(self.get_all_cleaned_data())

        return context
    '''
    def get_step_url(self, step):
        return reverse(self.url_name, kwargs={'step': step})

    def get_template_names(self):
        #print(TEMPLATES[self.steps.current])
        return [TEMPLATES[self.steps.current]]






    def get_context_data(self, **kwargs):
        context = super(ProfileFormWizardView, self).get_context_data(**kwargs)
        #context['all_data'] = self.get_all_cleaned_data()
        #prefix = super(ProfileFormWizardView, self).get_form_prefix(step=None, form=None)
        #context=super(ProfileFormWizardView, self).get_context_data(**kwargs)
        #print (self.form_list)
        #data = self.get_cleaned_data_for_step(prefix)
        data_dict = {}
        #print(self.request.POST.get('starter-profile_image',False))
        if self.request.POST.get('starter-profile_image',False) != False:
            self.image_name['name']=self.request.POST.get('starter-profile_image',False)



        print(self.request.POST.get('starter-profile_image',False))


        #print(self.get_cleaned_data_for_step('starter'))
        self.data_dict['starter']=self.get_cleaned_data_for_step('starter')

        self.data_dict['education']=self.get_cleaned_data_for_step('education')
        self.data_dict['first_education']=self.get_cleaned_data_for_step('first_education')
        self.data_dict['second_education']=self.get_cleaned_data_for_step('second_education')
        self.data_dict['employment']=self.get_cleaned_data_for_step('employment')
        self.data_dict['first_employment']=self.get_cleaned_data_for_step('first_employment')
        self.data_dict['second_employment']=self.get_cleaned_data_for_step('second_employment')
        #self.data_dict['hour_rate']=self.get_cleaned_data_for_step('hour_rate')
        self.data_dict['proficiency']=self.get_cleaned_data_for_step('proficiency')
        self.data_dict['location']=self.get_cleaned_data_for_step('location')


        #print(self.get_cleaned_data_for_step('starter'))
        #self.request.session['prof_title'] = self.get_cleaned_data_for_step('starter')
        #print(self.request.session['prof_title'])
        context['all_data']=self.data_dict

        #MONITOR
        #print(context)
        print(self.data_dict)

        #print(self.data_dict['location']['phone_number'].country_code)
        moderation(self.data_dict)


        return context

    def store_sessions(self, **kwargs):
        pass
        self.request.session['prof_title']=self.get_cleaned_data_for_step('starter')['prof_title']
        #print(self.request.session['prof_title'])

    def process_step(self, form):
        #print (self.get_form_step_data(form).keys())
        return self.get_form_step_data(form)

    def done(self,form_list,**kwargs):

        #print (form_list)
        form_data = [form.cleaned_data for form in form_list]

        form_dict=sort_forms_data(form_data)


        print(self.data_dict)

        #if self.data_dict['hour_rate'] != None:
        new_profile = EmployeeProfileModel(user = self.request.user,
                                            is_active = moderation(self.data_dict),
                                            status = self.data_dict['starter']['status'],
                                        prof_title = self.data_dict['starter']['prof_title'],
                                        prof_overview = self.data_dict['starter']['prof_overview'],




                                        language_compatancy = self.data_dict['proficiency']['language_compatancy'],
                                        #payment = self.data_dict['hour_rate']['payment'],
                                        category_industry = self.data_dict['proficiency']['category_industry'],
                                        #availability = self.data_dict['hour_rate']['availability'],
                                        address_1 = self.data_dict['location']['address_1'],
                                        #address_2 = self.data_dict['location']['address_2'],
                                        city = self.data_dict['location']['city'],
                                        zip_code = self.data_dict['location']['zip_code'],
                                        country = self.data_dict['location']['country'],
                                        phone=self.data_dict['location']['phone'],
                                        )
        new_profile.save()

        new_education = EduWizard(profile = new_profile,
                                  school = self.data_dict['education']['school'],
                                  started = self.data_dict['education']['started'],
                                  ended = self.data_dict['education']['ended'],
                                  degree = self.data_dict['education']['degree'],
                                  area_of_study = self.data_dict['education']['area_of_study'],
                                  Description = self.data_dict['education']['Description'],

                                 )
        new_education.save()
        if self.data_dict['first_education']!=None:
            new_education = EduWizard(profile = new_profile,
                                  school = self.data_dict['first_education']['school'],
                                  started = self.data_dict['first_education']['started'],
                                  ended = self.data_dict['first_education']['ended'],
                                  degree = self.data_dict['first_education']['degree'],
                                  area_of_study = self.data_dict['first_education']['area_of_study'],
                                  Description = self.data_dict['first_education']['Description'],

                                 )
            new_education.save()
        if self.data_dict['second_education']!=None:
            new_education = EduWizard(profile = new_profile,
                                  school = self.data_dict['second_education']['school'],
                                  started = self.data_dict['second_education']['started'],
                                  ended = self.data_dict['second_education']['ended'],
                                  degree = self.data_dict['second_education']['degree'],
                                  area_of_study = self.data_dict['second_education']['area_of_study'],
                                  Description = self.data_dict['second_education']['Description'],

                                 )
            new_education.save()


        new_employment = EmloymentWizard(profile = new_profile,
                                  company = self.data_dict['employment']['company'],
                                  title = self.data_dict['employment']['title'],
                                  location = self.data_dict['employment']['location'],
                                  country = self.data_dict['employment']['country'],
                                  role = self.data_dict['employment']['role'],
                                  period_sterted = self.data_dict['employment']['period_sterted'],
                                  month_started = self.data_dict['employment']['month_started'],
                                  period_ended = self.data_dict['employment']['period_ended'],
                                  month_ended = self.data_dict['employment']['month_ended'],
                                  is_current =self.data_dict['employment']['is_current'],
                                  description = self.data_dict['employment']['description'],

                                 )
        new_employment.save()

        if self.data_dict['first_employment']!=None:
            new_employment = EmloymentWizard(profile = new_profile,
                                  company = self.data_dict['first_employment']['company'],
                                  title = self.data_dict['first_employment']['title'],
                                  location = self.data_dict['first_employment']['location'],
                                             country=self.data_dict['employment']['country'],
                                             role=self.data_dict['employment']['role'],
                                             period_sterted=self.data_dict['employment']['period_sterted'],
                                             month_started=self.data_dict['employment']['month_started'],
                                             period_ended=self.data_dict['employment']['period_ended'],
                                             month_ended=self.data_dict['employment']['month_ended'],
                                  is_current =self.data_dict['first_employment']['is_current'],
                                  description = self.data_dict['first_employment']['description'],

                                 )
            new_employment.save()

        if self.data_dict['second_employment']!=None:
            new_employment = EmloymentWizard(profile = new_profile,
                                  company = self.data_dict['second_employment']['company'],
                                  title = self.data_dict['second_employment']['title'],
                                  location = self.data_dict['second_employment']['location'],
                                             country=self.data_dict['employment']['country'],
                                             role=self.data_dict['employment']['role'],
                                             period_sterted=self.data_dict['employment']['period_sterted'],
                                             month_started=self.data_dict['employment']['month_started'],
                                             period_ended=self.data_dict['employment']['period_ended'],
                                             month_ended=self.data_dict['employment']['month_ended'],
                                  is_current =self.data_dict['second_employment']['is_current'],
                                  description = self.data_dict['second_employment']['description'],

                                 )
            new_employment.save()

        #object = EmployeeProfileModel.objects.get(id=111)
        #return render_to_response('profiles/done.html',{'object':object})
        return render_to_response('profiles/done.html')



def ajax_post(request):
        #form = self.form_class(request.POST)
        print ("sgsgsgsgsgsgsg")
        if request.method == "POST" and request.is_ajax():
            print ("sgsgsgsgsgsgsg")
            get_value= request.POST
            #education=Education()
            #education.school=get_value
            #education.save
            #print(get_value)
            #print (request.body)



from .forms import PostJobForm
@method_decorator(login_required, name='dispatch')
class PostJobView(TemplateView):
    template_name = 'profiles/post_job/jobpost.html'
    template_name_done = 'profiles/done.html'
    form_class = PostJobForm

    def get(self,request):
        form = self.form_class
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        print (form)



        if form.is_valid():
            jobpost = form.save(commit=False)
            #print (jobpost)
            data=form.cleaned_data
            #print(data)
            #print(data['deadline'])
            jobpost.user = request.user
            jobpost.is_active = job_moderation(data)
            jobpost.save()

            return render(request,self.template_name_done,{})
        return render(request, self.template_name, {'form': form})


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#


from django.db.models import Q # new
from .forms import BudgetWizardForm, \
                    DescriptionWizardForm,\
                    DetailsWizardForm,\
                    ExpertiseWizardForm,\
                    TitleWizardForm,\
                    ReviewWizardForm,\
                    VisibilityWizardForm,\
                    IndexWizardForm


JOBPOSTFORMS = [
    ('index',IndexWizardForm),
('title',TitleWizardForm),
('description',DescriptionWizardForm),
('detials',DetailsWizardForm),
('expertise',ExpertiseWizardForm),
('visibility',VisibilityWizardForm),
('budget',BudgetWizardForm),
('review',ReviewWizardForm)
]


JOBPOSTTEMPLATES = {
    'index':"profiles/job_post_wizard/header_footer_in.html",
    'title':"profiles/job_post_wizard/title.html",
    'description': "profiles/job_post_wizard/Description.html",
    'detials': "profiles/job_post_wizard/details.html",
    'expertise': "profiles/job_post_wizard/Expertise.html",
    'visibility': "profiles/job_post_wizard/visibility.html",
    'budget': "profiles/job_post_wizard/budget.html",
    'review': "profiles/job_post_wizard/review.html",
}

from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class JobPostWizardWiew(NamedUrlSessionWizardView):
    pass

    def get_step_url(self, step):
        return reverse(self.url_name, kwargs={'step': step})

    def get_template_names(self):
        #print(TEMPLATES[self.steps.current])
        return [JOBPOSTTEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        pass
        return render_to_response('profiles/job_post_wizard/done.html', {})


# class FreelancerListView(ListView):
#     model = EmployeeProfileModel
#     education_model = EduWizard
#     template_name = 'profiles/freelancerlistview/settings.html'
#
#     def get_queryset(self): # new
#
#         #result =EmployeeProfileModel.objects.filter(prof_title__icontains='Web')
#         result = EmployeeProfileModel.objects.all()
#         #education = EduWizard.objects.all()
#         #profile_edu = EduWizard.objects.filter(profile=result[1])
#         #print (education[0].profile)
#         #print (result[0])
#         #print(profile_edu)
#         #print (result)
#         for profile in result:
#             profile_edu = EduWizard.objects.filter(profile=profile)
#             print(profile_edu)
#             print(profile.id)
#
#         return result
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import SearchForm
class FreelancerListPagView(ListView):
    model = EmployeeProfileModel
    form_class = SearchForm
    initial = {'key': 'value'}

    template_name = 'profiles/freelancerlistview/freelancerlist.html'
    context_object_name = 'freelancers'
    paginate_by = 3
    #queryset = EmployeeProfileModel.objects.all()
    #queryset = EmployeeProfileModel.objects.filter(status='')

    def get(self,request,**kwargs):
        form = self.form_class(initial=self.initial)
        #context = super(FreelancerListPagView, self).get(**kwargs)

        print(kwargs['slug'].capitalize())
        #print (queryset)
        if kwargs['slug'] == 'all':
            queryset = EmployeeProfileModel.objects.all()
            return render(request,self.template_name,{'objects':queryset,'form':form})
        elif kwargs['slug'] == 'freelancer':
            print('asdasdasd')
            queryset = EmployeeProfileModel.objects.filter(status__in=['Freelancer','Both'])
            #queryset = EmployeeProfileModel.objects.filter(status='Freelancer')
            print(queryset)
            return render(request, self.template_name, {'objects': queryset, 'form': form})
        elif kwargs['slug'] == 'full time':
            print('asdasdasd')
            queryset = EmployeeProfileModel.objects.filter(status__in=['Fulltime','Both'])
            print(queryset)
            return render(request, self.template_name, {'objects': queryset, 'form': form})



    # def get_context_data(self,**kwargs):
    #
    #     context = super(FreelancerListPagView,self).get_context_data(**kwargs)
    #     form = self.form_class(initial=self.initial)
    #     context['form']=form
    #     print(kwargs)
    #     return context

    # def get(self,request):
    #     print(self.context)
    #     return render(request,self.template_name, self.context)

    # def get_queryset(self): # new
    #
    #     #result =EmployeeProfileModel.objects.filter(prof_title__icontains='Web')
    #     result = EmployeeProfileModel.objects.all()
    #     page = self.request.GET.get('page', 1)
    #     paginator = Paginator(result, 3)
    #
    #     #results = paginator.get_page(page)
    #     try:
    #         results = paginator.page(page)
    #     except PageNotAnInteger:
    #         results = paginator.page(1)
    #     except EmptyPage:
    #         results = paginator.page(paginator.num_pages)
    #
    #
    #     # for profile in result:
    #     #     profile_edu = EduWizard.objects.filter(profile=profile)
    #     #     print(profile_edu)
    #     #     print(profile.id)
    #     context={'results':results}
    #
    #     #return results
    #     return render(self.request,self.template_name,{"results":results})

class FreelancerDetailView(TemplateView):
    template_name = 'profiles/freelancerlistview/members.html'
    model = EmployeeProfileModel






    def get_context_data(self, **kwargs):
        context = super(FreelancerDetailView,self).get_context_data(**kwargs)

        #context['now'] = timezone.now()
        

        context['profile'] = EmployeeProfileModel.objects.get(id=context['id'])

        profile = context['profile']
        print (profile)
        context['education'] = EduWizard.objects.filter(profile=profile)

        context['employment'] = EmloymentWizard.objects.filter(profile=profile)
        #print(profile[0].get_absolute_url())
        #print(context['employment'][0].role)
        print(context['employment'])
        print(context['education'])

        
        return context

class SearchResultsView(ListView):
    initial = {'key':'value'}
    model = EmployeeProfileModel
    form_class = SearchForm
    template_name = 'profiles/freelancerlistview/freelancersearch.html'
    #template_name = 'profiles/joblist/jobsearch.html'
    paginate_by = 3
    template_joblist = 'profiles/joblist/jobsearch.html'
    context_object_name = "profile"

    def get_context_data(self,**kwargs):

        context = super(SearchResultsView,self).get_context_data(**kwargs)
        form = self.form_class(initial=self.initial)

        context['form']=form

        query = self.request.GET.get('q', '')
        #status = self.request.GET.get('status', '')
        location = self.request.GET.get('location', '')
        context['query'] = query
        #context['status'] = status
        context['location'] = location


        #print (context)


        return context

    def get_queryset(self):
        query = self.request.GET.get('q','')
        status = self.request.GET.get('status','')
        location = self.request.GET.get('location','')
        #print (status)
        #print (query)
        #print (location)
        if self.request.user.status == 'Job Seeker':
            self.template_name = self.template_joblist
            return PostJob.objects.filter(Q(job_title__icontains=query, country__icontains=location, ),
                                          is_active=True, )
        elif self.request.user.status == 'Employer':

            return EmployeeProfileModel.objects.filter(Q(prof_title__icontains=query, country__icontains=location, ),
                                                       is_active=True, )










from .models import PostJob
class JobListView(ListView):
    template_name = 'profiles/joblist/joblist.html'
    model = PostJob
    form_class = SearchForm
    initial = {'key':'value'}
    context_object_name = 'jobs'
    paginate_by = 3


    def get_context_data(self,**kwargs):
        print(self.kwargs)
        context = super(JobListView,self).get_context_data(**kwargs)
        form = self.form_class(initial=self.initial)
        #queryset = PostJob.objects.all()
        #fultime = kwargs['slug']
        #print(selfkwargs)
        if self.kwargs['slug'] == 'all':
            queryset = PostJob.objects.all()
            context['jobs'] = queryset
            print(context)

        else :


            queryset = PostJob.objects.filter(Status = self.kwargs['slug'] )
            print(queryset)
            print((self.kwargs['slug']))
            context['jobs'] = queryset
        context['form']=form
        print(context)
        return context

    # def get_queryset(self): # new
    #
    #     #result =EmployeeProfileModel.objects.filter(prof_title__icontains='Web')
    #     result = self.model.objects.all()
    #     #education = EduWizard.objects.all()
    #     #profile_edu = EduWizard.objects.filter(profile=result[1])
    #     #print (education[0].profile)
    #     #print (result[0])
    #     #print(profile_edu)
    #     #print (result)
    #
    #     for job in result:
    #         print (job.id)
    #
    #     return result


class JobDetailView(TemplateView):
    template_name = 'profiles/joblist/jobdetail.html'
    model = PostJob

    def get_context_data(self, **kwargs):
        context = super(JobDetailView,self).get_context_data(**kwargs)
        print(context)

        query = JobApply.objects.filter(applier = self.request.user,job = kwargs['id'])
        print (query)
        print(kwargs)
        apply = True

        if query:
            apply = False


        context['apply'] = apply
        # context['now'] = timezone.now()
        #print (context)


        context['profile'] = PostJob.objects.get(id=context['id'])

        return context



        #profile = context['profile']
        #print(profile)
#context['education'] = EduWizard.objects.filter(profile=profile)
#context['employment'] = EmloymentWizard.objects.filter(profile=profile)
# print(profile[0].get_absolute_url())
# print(context['employment'][0].role)










class ProfileTest(TemplateView):

    initial = {'key': 'value'}
    template_name = 'profiles/tests/starter.html'
    template_done = 'profiles/tests/done.html'
    form_class = ProfileForm1

    def get(self,request):
        return render(request, self.template_name, {'form':self.form_class})

    def post(self,request):
        if request.method == 'POST':
            form = ProfileForm1(request.POST,request.FILES)
            print (request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            print(data['profile_image'])
            print(self.request.user)
            new_profile = EmployeeProfileModel(user=request.user,prof_title=data['prof_title'],
                                            prof_overview=data['prof_overview'],
                                            profile_image=data['profile_image'])
            new_profile.save()
        return redirect(reverse('profile_wizard:detile'))

class ProfileTestDetile(TemplateView):
    template_name = 'profiles/tests/done.html'
    def get(self,request):
        object = EmployeeProfileModel.objects.get(id=105)
        print (object.prof_title)
        return render(request,self.template_name,{'object':object})
from users import models as usermodel
from users import forms
#@method_decorator(login_required, name='dispatch')

class SettingsView(TemplateView):
    template_name = 'profiles/settings/settings.html'
    template_name_individual = 'profiles/settings/company/company.html'
    initial = {'key': 'value'}
    form_class = forms.RegistrationForm
    location_form = LocationWizardForm
    edit_form = forms.EditProfileForm

    def post(self,request,**kwargs):
        form = self.edit_form(request.POST,instance=request.user)
        #print(form)
        if form.is_valid():
            form.save()
            data=form.cleaned_data
            messages.success(request, 'Your password was updated successfully!')
            print(messages)
            #print(data)

        #return HttpResponse('asdasd')
        #return render(request, self.template_name, {'edit_form': edit_form, 'user': user, 'form': form, })
        return redirect('profile_wizard:settings')


    def get(self,request,**kwargs):
        user = request.user
        form = self.form_class(initial=self.initial)
        location_form = self.location_form
        edit_form = self.edit_form(request.POST,instance=request.user)
        form_change = forms.UserChangeForm(request.POST, instance=request.user)
        print(user.id)
        print(user.status)
        return render(request, self.template_name,
                      {'edit_form': edit_form, 'user': user, 'form': form})



class UserPassChange(TemplateView):
    form_class = forms.PasswordChangeForm
    template_name = 'users/passchange.html'
    def get(self,request):
        form = self.form_class(data=request.POST,user=request.user)
        return render(request, self.template_name,{'form':form})
    def post(self,request):
        form = self.form_class(data=request.POST,user=request.user)
        print(form)
        if form.is_valid():
            data=form.cleaned_data
            print(data)
            update_session_auth_hash(request,form.user)
            form.save()

            return redirect('home:index')
        return render(request, self.template_name,{'form':form})

from .forms import CompanyForm
from django.urls import reverse_lazy
class EmployerProfileReview(UpdateView):
    template_name = 'profiles/settings/company/review.html'
    template_name_fill = 'profiles/settings/company/fill_company.html'
    #form_class = CompanyForm
    initial = {'key':'value'}
    model = Company
    fields = ['company_name','company_description','website','contact_person_name','phone','email']
    success_url = reverse_lazy('profile_wizard:settings')


    def get_context_data(self, **kwargs):
        data = super(EmployerProfileReview, self).get_context_data(**kwargs)
        print(self.request)
        print(self.kwargs)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        form.save()

        return super(EmployerProfileReview, self).form_valid(form)


    def form_invalid(self,form):
        print('form_is invalid')
        return super(EmployerProfileReview, self).form_invalid(form)

class CompanyCreate(UpdateView):
    template_name = 'profiles/settings/company/review.html'
    template_name_fill = 'profiles/settings/company/fill_company.html'
    form_class = CompanyForm
    initial = {'key':'value'}
    model = Company
    #fields = ['company_name']
    def get(self,request,**kwargs):

        # if kwargs['slug'] == 'review':
        #     return render(request, self.template_name, {})
        # elif kwargs['slug'] == 'fill':
        form = self.form_class(initial=self.initial)
        return render(request,self.template_name_fill,{'form':form})


    def post(self,request,**kwargs):
        form = self.form_class(data=request.POST)
        print(form)
        if form.is_valid():
            data = form.cleaned_data
            company = Company(user=request.user,
                                company_name=data['company_name'],
                              company_description = data['company_description'],
                              website = data['website'],
                              contact_person_name = data['contact_person_name'],
                              phone = data['phone'],
                              email = data['email'])
            company.save()
            print(data)
            #print(request.user)
            comp_obj = Company.objects.filter(user=request.user)
            if comp_obj:
                id = comp_obj[0].id
            return redirect('profile_wizard:employer_review',id)
        return HttpResponse('ar aitvirta')


class MyJobs(TemplateView):
    model = PostJob
    template_name = 'profiles/myjobs/myjobs.html'
    def get(self,request,**kwargs):
        queryset = self.model.objects.filter(user=request.user,is_active = True)
        appliers = JobApply.objects.filter(jobowner=self.request.user)
        print(queryset[0].category)
        print(len(appliers))
        lenn = len(appliers)
        return render(request,self.template_name,{'jobs':queryset,'lenn':lenn})





