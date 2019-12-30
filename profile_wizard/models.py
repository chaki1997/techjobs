from django.db import models
from django.utils.translation import ugettext as _
from users.models import CustomUser
from .utils import get_image_path
from django.conf import settings
from .choices import LENGUAGE_CHOICES,YEAR_FROM,YEAR_TO,ROLE,AVAILABILITY, MONTH,OPTION
from django.db import models
from phone_field import PhoneField
from phonenumber_field.modelfields import PhoneNumberField
from users.models import CustomUser
from .category import CATEGORY




class EmployeeProfileModel(models.Model):

    #System referance fields
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='EmployeeID',on_delete=models.CASCADE,null=True, blank=True)
    is_active = models.BooleanField(default=True)

    #ProfileForm1
    status = models.CharField(choices=OPTION,max_length=64, blank=False, default='empty')
    prof_title = models.CharField(max_length=64, blank=True, null=True)
    prof_overview = models.TextField(blank=True, null=True)

    #ProfileForm3
    availability = models.CharField(choices=AVAILABILITY, max_length=64, blank=True, )
    payment = models.IntegerField(default=12345)

    #ProficiencyWizardForm
    category_industry = models.CharField(choices=CATEGORY,max_length=64,blank=True,)
    language_compatancy = models.CharField(choices=LENGUAGE_CHOICES, blank=True, max_length=255)

    #location formfields
    address_1 = models.CharField(_("address"), max_length=128,default='unknown')
    address_2 = models.CharField(_("address cont'd"), default='unknown',max_length=128, blank=True)
    city = models.CharField(_("city"), max_length=64,default='unknown')
    zip_code = models.CharField(_("zip code"), max_length=5,default=12345)
    country =  models.CharField(_("country"), default='unknown',max_length=128)
    phone = models.CharField(_("phone"), default='unknown',max_length=128)


    class Meta:
        ordering = ['-id']

    def __unicode__(self):
        return self.user

    @models.permalink
    def get_absolute_url(self):
        return ("profile_wizard:profile-detail", [self.id, ])

    # def __str__(self):
    #   return self










# Create your models here.
#settings.AUTH_USER_MODEL
from django.core.files.storage import FileSystemStorage
fs = FileSystemStorage(location='/media/photos')
class FreeProfileWizard(models.Model):
    #Referance to User
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='freelancerID',on_delete=models.CASCADE,
    limit_choices_to={'is_staff': True},null=True, blank=True)
    is_active = models.BooleanField(default=True)
    status = models.CharField(max_length=64, blank=False, default='empty')
    # Upload profile avatar
    profile_image = models.ImageField(storage = fs,upload_to=get_image_path, null=True,)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    # Professional Title
    prof_title = models.CharField(max_length=64, blank=True, null=True)
    #Profesional Overview
    prof_overview = models.TextField(blank=True, null=True)
    #Language compatancy
    language_compatancy = models.CharField(choices=LENGUAGE_CHOICES, blank=True,max_length=255)
    #Education
    education = models.CharField(max_length=1024,blank=True)
    hourly_rate = models.IntegerField(default=12345)
    category_industry = models.CharField(choices=CATEGORY,max_length=64,blank=True,)
    #location formfields
    availability = models.CharField(choices=AVAILABILITY,max_length=64,blank=True,)
    address_1 = models.CharField(_("address"), max_length=128,default='unknown')
    address_2 = models.CharField(_("address cont'd"), default='unknown',max_length=128, blank=True)
    city = models.CharField(_("city"), max_length=64,default='unknown')
    zip_code = models.CharField(_("zip code"), max_length=5,default=12345)
    country =  models.CharField(_("country"), default='unknown',max_length=128)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    phone_number = PhoneNumberField(null=True, blank=True, unique=False)

    class Meta:
        ordering = ['-id']

    #def __str__(self):
     #   return self
    def __unicode__(self):
        return self.user

    @models.permalink
    def get_absolute_url(self):
        return ("profile_wizard:profile-detail", [self.id, ])

class PostJob(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='postjobID', on_delete=models.CASCADE,
                             limit_choices_to={'is_staff': True},null=True, blank=True)
    is_active = models.BooleanField(default=True)
    Status = models.CharField(max_length=64, blank=False,default='empty')
    job_title = models.CharField(max_length=64, blank=True, null=True)
    prof_description = models.TextField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY, max_length=128, blank=True, )
    country = models.CharField(_("country"), default='unknown', max_length=128)
    budjet = models.IntegerField(default=12345)
    deadline = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __unicode__(self):
        return self.user

    @models.permalink
    def get_absolute_url(self):
        return ("profile_wizard:job-detail", [self.id, ])
    



class EducationWizard(models.Model):
    profile = models.ForeignKey(EmployeeProfileModel,related_name='EmployeeID',on_delete=models.CASCADE)
    school = models.CharField(max_length=128,blank=True,)
    started = models.CharField(choices=YEAR_FROM,max_length=64,blank=True,)
    ended = models.CharField(choices=YEAR_TO, blank=True,max_length=255)
    degree = models.CharField(blank=True,max_length=255)
    area_of_study =  models.CharField(max_length=256,blank=True,)
    Description = models.CharField(max_length=1024,blank=True,)

    school_second = models.CharField(max_length=128,blank=True,)
    started_second = models.CharField(choices=YEAR_FROM,max_length=64,blank=True,)
    ended_second = models.CharField(choices=YEAR_TO, blank=True,max_length=255)
    degree_second = models.CharField(blank=True,max_length=255)
    area_of_study_second =  models.CharField(max_length=256,blank=True,)
    Description_second = models.CharField(max_length=1024,blank=True,)

    def __unicode__(self):
        return self.user

class EduWizard(models.Model):
    profile = models.ForeignKey(EmployeeProfileModel,related_name='freeID',on_delete=models.CASCADE)
    school = models.CharField(max_length=128,blank=True,)
    started = models.CharField(choices=YEAR_FROM,max_length=64,blank=True,)
    ended = models.CharField(choices=YEAR_TO, blank=True,max_length=255)
    degree = models.CharField(blank=True,max_length=255)
    area_of_study =  models.CharField(max_length=256,blank=True,)
    Description = models.CharField(max_length=1024,blank=True,)
    def __unicode__(self):
        return self.profile


class EmloymentWizard(models.Model):
    profile = models.ForeignKey(EmployeeProfileModel,related_name='ProfileID',on_delete=models.CASCADE)
    company = models.CharField(max_length=128,blank=True,)
    title = models.CharField(max_length=128,blank=True,)
    location = models.CharField(max_length=128,blank=True,)
    country = models.CharField(max_length=128, blank=True, )
    role =  models.CharField(choices=CATEGORY, max_length=128,blank=True,)
    period_sterted = models.CharField(choices=YEAR_FROM,max_length=64,blank=True,)
    month_started = models.CharField(choices=MONTH, max_length=64, blank=True, )
    period_ended = models.CharField(choices=YEAR_TO, blank=True,max_length=64)
    month_ended = models.CharField(choices=MONTH, max_length=64, blank=True, )
    is_current = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.profile

class Company(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='company_user', on_delete=models.CASCADE,null=True, blank=True)
    company_name = models.CharField(max_length=128,blank=True,)
    company_description = models.TextField(blank=True)
    website = models.CharField(max_length=128,blank=True,)
    contact_person_name = models.CharField(max_length=128,blank=True,)
    phone = models.CharField(max_length=128,blank=True,)
    email = models.EmailField(max_length=70,blank=True)

    def __unicode__(self):
        return self.company_name