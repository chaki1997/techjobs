from django import forms
from django.utils.translation import ugettext as _
from .utils import get_image_path
from .fields import ListTextWidget
from phonenumber_field.formfields import PhoneNumberField
from .models import \
    FreeProfileWizard,\
    EmloymentWizard,\
    EduWizard,\
    Company,\
    EmployeeProfileModel

from .choices import \
    LENGUAGE_CHOICES,\
    YEAR_FROM,\
    YEAR_TO,\
    ROLE,\
    AVAILABILITY,\
    STATUS,\
    DEGREE,\
    OPTION,\
    MONTH,\
    PHONE_INDEX

from .category import CATEGORY



class ProfileForm1(forms.ModelForm):


    status = forms.ChoiceField(choices = OPTION,required=False,widget=forms.Select(attrs={'name':"",'class':'','id':"", 'style':"width:30%;"}))

    prof_title = forms.CharField(label='Title',
            widget=forms.TextInput(attrs={'onclick':"add(id)",'class':'C#_developer','placeholder': "Example: Backend Developer "}))

    prof_overview = forms.CharField(required=False,
                                    widget=forms.Textarea(attrs={'onclick':"add(id)","rows":10, "cols":60,"placeholder":"Highlight your top skills, experience, and interests. "
                                                                                                    "This is one of the first things clients will see "
                                                                                                    "on your profile",
                                                                 "id":'text_area',
                                                                 "name":'textarea'
                                                                 }))
    #profile_image  = forms.ImageField(required=False, widget=forms.FileInput(attrs={"type":'file',"id":'imgInp' }))
    class Meta:
        model = EmployeeProfileModel
        fields = ('prof_title','prof_overview', )



DEGREE
class EducationWizardForm(forms.Form):
    school = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':' ','style': 'display:block','class':'first_scenario','id':'input_school',}))
    started = forms.ChoiceField(required=False,choices = YEAR_FROM, label="",
        widget=forms.Select(attrs={'placeholder':'years','class':'first_scenario','id':'input_select_form','placeholder':'FROM','lable':'asdasd'}))

    ended = forms.ChoiceField(required=False,choices = YEAR_TO, label="",  widget=forms.Select(attrs={'class':'first_scenario','id':'input_select_form_2','placeholder':'TO',}))
    degree = forms.ChoiceField(required=False, choices=DEGREE, label="",
                               widget=forms.Select(
                                   attrs={'class': 'first_scenario', 'id': 'input_select_form', 'placeholder': 'FROM',
                                          'lable': 'asdasd'}))
    #degree = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'first_scenario','id':'input_degree','type':'text' , 'name':'input_degree',}))
    area_of_study =  forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'first_scenario','type':'text','name':'Area_of_study','id':'Area_of_study'}))
    Description = forms.CharField(required=False,widget=forms.Textarea(attrs={'class':'first_scenario','name':'Description','id':'input_desctiption','cols':'69','rows':'10'}))
    repeat = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'id':'checkbox','style': 'display:none'}))
    "'style': 'display:none'"
    class Meta:
        model = EduWizard
        fields = ('repeat','school','started','ended','degree','area_of_study','Description', )




class ProfileForm3(forms.ModelForm):
    availability = forms.ChoiceField(choices=AVAILABILITY, label="",
                                     widget=forms.Select(attrs={"class": 'select_profiction'}))
    payment =forms.IntegerField(widget=forms.TextInput(attrs={'class':'input_price','placeholder':'0.00','onchange':"vatCalculation()",'id':"subtotal"}))
    #language_compatancy = forms.ChoiceField(choices = LENGUAGE_CHOICES, label="",  widget=forms.Select(attrs={"class":'select_profiction'}))
    #repeat = forms.BooleanField(required=False)


    class Meta:
        model = EmployeeProfileModel
        fields = ('availability','payment', )

class ProficiencyWizardForm(forms.ModelForm):

    language_compatancy = forms.ChoiceField(choices = LENGUAGE_CHOICES, label="",  widget=forms.Select(attrs={"class":'select_profiction'}))
    category_industry = forms.ChoiceField(choices=CATEGORY, widget=forms.Select(attrs={'class':'select_category'}))
    #repeat = forms.BooleanField(required=False)


    class Meta:
        model = EmployeeProfileModel
        fields = ('language_compatancy', )

class LocationWizardForm(forms.ModelForm):

    #availability = forms.ChoiceField(choices = AVAILABILITY, label="",  widget=forms.Select(attrs={"class":'select_profiction'}))
    address_1 = forms.CharField(required=False, max_length=128,widget=forms.TextInput(attrs={'type':'text','name':'address_1', 'placeholder':'Address'}))
    #address_2 = forms.CharField(required=False, max_length=128, widget=forms.TextInput(attrs={'type':'text','name':'address_2'}))
    city = forms.CharField(required=False, max_length=64,widget=forms.TextInput(attrs={'type':'text','name':'city','placeholder':'City'}))
    zip_code = forms.CharField(required=False, max_length=5,widget=forms.TextInput(attrs={'class':'postal_input','type':'text','name':'Postal Code', 'placeholder':'Zip'}))
    country =  forms.CharField(required=False, max_length=128,widget=forms.TextInput(attrs={'class':'select_input_1','type':'text','name':'Country','placeholder':'Country'}))

    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={'type':'hidden',
                'placeholder': '',
                #'autocomplete': 'off',
                'id':'phone_monitor'
            }
        ),
        required=False,)
    #phone_number = PhoneNumberField(required=False,widget=forms.TextInput(attrs={'id':'phonenumebr'}))

    class Meta:
        model = EmployeeProfileModel
        fields = ('language_compatancy',)




#forms.TextInput(attrs={'placeholder':"Highlight your top skills, experience, and interests. This is one of the first things clients will see on your profile"}))

class EmplymentFormWizard(forms.Form):

    company = forms.CharField(widget=forms.TextInput(attrs={'type':'text','name':'company','id':'input_Company'}))
    title = forms.CharField(required=True,widget=forms.TextInput(attrs={'type':'text','name':'input_degree','id':'input_degree_2'}))
    location = forms.CharField(required=False,widget=forms.TextInput(attrs={'type':'text','placeholder':'City','id':'Location_input'}))
    country = forms.CharField(required=False,widget=forms.TextInput(attrs={'type':'hidden','placeholder':'country','id':'monitor_country'}))
    role =  forms.ChoiceField(required=True,choices=CATEGORY, widget=forms.Select(attrs={'id':'select_Role'}))
    period_sterted = forms.ChoiceField(required=True,choices=YEAR_FROM,widget=forms.Select(attrs={'id':'select_Role_month','class':'col-md-5 '}))
    month_started = forms.ChoiceField(required=True, choices=MONTH, widget=forms.Select(
        attrs={'id': 'from_month', 'class': 'col-md-5 offset-1'}))
    period_ended = forms.ChoiceField(required=False,choices=YEAR_TO,widget=forms.Select(attrs={'id':'select_Role_month','class':'col-md-5 '}))
    month_ended = forms.ChoiceField(required=False, choices=MONTH, widget=forms.Select(
        attrs={'id': 'to_month', 'class': 'col-md-5 offset-1'}))
    is_current = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'type':'checkbox'}))
    description = forms.CharField(required=False,widget=forms.Textarea(attrs={'class':'first_scenario','name':'Description','id':'input_desctiption','cols':'69','rows':'10'}))
    repeat = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'id':'checkbox','style':'display:none'}))
    class Meta:
        model = EmloymentWizard
    {'key':'value'}







#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
from .models import PostJob
class PostJobForm(forms.ModelForm):
    Status = forms.CharField(widget=forms.TextInput(attrs={'type':"hidden",'name':"fname", 'id':"input", 'value':""}))
    job_title = forms.CharField(label='Title',
            widget=forms.TextInput(attrs={'class':'title','placeholder': "","value":''}))
    prof_description = forms.CharField(required=False,
                                    widget=forms.Textarea(attrs={"rows":10, "cols":100,"placeholder":"",
                                                                 "id":'',
                                                                 "name":'tescription'
                                                                 }))
    category = forms.ChoiceField(required=False,choices=CATEGORY, widget=forms.Select(attrs={'id':'select_Role'}))

    country = forms.CharField(required=False,max_length=128,widget=forms.TextInput(attrs={'class':'select_input_1','type':'text','name':'Country','placeholder':'City'}))
    budjet = forms.IntegerField(widget=forms.TextInput(attrs={'class':'input_price','placeholder':'0', 'id':'price'}))
    deadline = forms.DateField(widget=forms.TextInput(attrs={"type":'date',"id":'deadline'}))

    class Meta:
        model = PostJob
        fields = ('Status','job_title','prof_description','country','budjet','category')



#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

class SearchForm(forms.Form):
    #status = forms.ChoiceField(choices=STATUS,widget=forms.Select(attrs={}))
    status = forms.ChoiceField(choices=STATUS, widget=forms.Select(attrs={}))
    location = forms.CharField(required=False,max_length=128, widget=forms.TextInput(attrs={'placeholder':"Search Location"}))


from django.forms.widgets import Input


class TelInput(Input):
    input_type = 'tel'


class CompanyForm(forms.Form):

    company_name = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'id':"name_monitor",'type':"text", 'name':"name", 'value':"", 'placeholder':"Company Name"}) )
    company_description = forms.CharField(widget=forms.Textarea(attrs={'name':"descriptiom", 'id':"company_description", 'cols':"60",'rows':"10", 'placeholder':"Company Description",'maxlength':"200"}))
    website = forms.CharField(max_length=128,  widget=forms.TextInput(attrs={'type':"text",'name':"Website",'value':"", 'placeholder':"Website"}) )
    contact_person_name = forms.CharField(max_length=128,  widget=forms.TextInput(attrs={'type':"text",'name':"name",'value':"", 'placeholder':"Name"}) )
    #phone = forms.CharField(max_length=128,  widget=forms.TextInput(attrs={'type':"tel", 'name':"tel" ,'value':"" ,'placeholder':"Tel" }))
    email = forms.EmailField(max_length=70,  widget=forms.TextInput(attrs={'type':'email','placeholder':"email"}))
    phone = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'placeholder': '',
                'autocomplete': 'off',
                'id':'iphone'
            }
        ),
        required=False,)


    class Meta:
        model = Company

class EmployeeEditForm(forms.Form):
    status = forms.ChoiceField(choices=OPTION, required=False,
                               widget=forms.Select(attrs={'name': "", 'id': "", 'style': "width:30%;"}))

    prof_title = forms.CharField(label='Title',
                                 widget=forms.TextInput(attrs={'onclick': "add(id)", 'class': 'C#_developer',
                                                               'placeholder': "Example: Backend Developer"}))

    prof_overview = forms.CharField(required=False,
                                    widget=forms.Textarea(attrs={'onclick': "add(id)", "rows": 10, "cols": 60,
                                                                 "placeholder": "Highlight your top skills, experience, and interests. "
                                                                                "This is one of the first things clients will see "
                                                                                "on your profile",
                                                                 "id": 'text_area',
                                                                 "name": 'textarea'
                                                                 }))

    # profile_image  = forms.ImageField(required=False, widget=forms.FileInput(attrs={"type":'file',"id":'imgInp' }))

    #EDUCATION
    school = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'display:block', 'class': 'first_scenario', 'id': 'input_school', }))
    started = forms.ChoiceField(required=False, choices=YEAR_FROM, label="",
                                widget=forms.Select(
                                    attrs={'placeholder': 'years', 'class': 'first_scenario', 'id': 'input_select_form',
                                           'placeholder': 'FROM', 'lable': 'asdasd'}))

    ended = forms.ChoiceField(required=False, choices=YEAR_TO, label="", widget=forms.Select(
        attrs={'class': 'first_scenario', 'id': 'input_select_form_2', 'placeholder': 'TO', }))
    degree = forms.ChoiceField(required=False, choices=DEGREE, label="",
                               widget=forms.Select(
                                   attrs={'class': 'first_scenario', 'id': 'input_select_form', 'placeholder': 'FROM',
                                          'lable': 'asdasd'}))
    # degree = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'first_scenario','id':'input_degree','type':'text' , 'name':'input_degree',}))
    area_of_study = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'first_scenario', 'type': 'text', 'name': 'Area_of_study', 'id': 'Area_of_study'}))
    Description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={'class': 'first_scenario', 'name': 'Description', 'id': 'input_desctiption', 'cols': '69',
               'rows': '10'}))
    repeat = forms.BooleanField(required=False,
                                widget=forms.CheckboxInput(attrs={'id': 'checkbox', 'style': 'display:none'}))
    #EMPLOYMENT

    company = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'name': 'company', 'id': 'input_Company'}))
    title = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'type': 'text', 'name': 'input_degree', 'id': 'input_degree_2'}))
    location = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'type': 'text', 'placeholder': 'City', 'id': 'Location_input'}))
    role = forms.ChoiceField(required=False, choices=CATEGORY, widget=forms.Select(attrs={'id': 'select_Role'}))
    period_sterted = forms.ChoiceField(required=False, choices=YEAR_FROM, widget=forms.Select(
        attrs={'id': 'select_Role_month', 'class': 'col-md-5 offset-1'}))
    period_ended = forms.ChoiceField(required=False, choices=YEAR_TO, widget=forms.Select(
        attrs={'id': 'select_Role_month', 'class': 'col-md-5 offset-1'}))
    is_current = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'type': 'checkbox'}))
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={'class': 'first_scenario', 'name': 'Description', 'id': 'input_desctiption', 'cols': '69',
               'rows': '10'}))
    repeat = forms.BooleanField(required=False,
                                widget=forms.CheckboxInput(attrs={'id': 'checkbox', 'style': 'display:none'}))

    #HOUR_RATE

    availability = forms.ChoiceField(choices=AVAILABILITY, label="",
                                     widget=forms.Select(attrs={"class": 'select_profiction'}))
    hourly_rate = forms.IntegerField(widget=forms.TextInput(
        attrs={'class': 'input_price', 'placeholder': '0.00', 'onchange': "vatCalculation()", 'id': "subtotal"}))

    #PROFICIANCY

    language_compatancy = forms.ChoiceField(choices=LENGUAGE_CHOICES, label="",
                                            widget=forms.Select(attrs={"class": 'select_profiction'}))
    category_industry = forms.ChoiceField(choices=CATEGORY, widget=forms.Select(attrs={'class': 'select_category'}))

    #LOCATION

    address_1 = forms.CharField(required=False, max_length=128,
                                widget=forms.TextInput(attrs={'type': 'text', 'name': 'address_1'}))
    address_2 = forms.CharField(required=False, max_length=128,
                                widget=forms.TextInput(attrs={'type': 'text', 'name': 'address_2'}))
    city = forms.CharField(required=False, max_length=64, widget=forms.TextInput(
        attrs={'type': 'text', 'name': 'city', 'placeholder': 'start typing your city'}))
    zip_code = forms.CharField(required=False, max_length=5, widget=forms.TextInput(
        attrs={'class': 'postal_input', 'type': 'text', 'name': 'Postal Code'}))
    country = forms.CharField(required=False, max_length=128, widget=forms.TextInput(
        attrs={'class': 'select_input_1', 'type': 'text', 'name': 'Country', 'placeholder': 'Country'}))

    #phone_number = PhoneNumberField(required=False, widget=forms.TextInput(attrs={'id': 'phonenumebr'}))
    phone = forms.IntegerField(widget=forms.TextInput())
    class Meta:
        model = EmployeeProfileModel

class TitleWizardForm(forms.Form):
    pass

class DescriptionWizardForm(forms.Form):
    pass

class DetailsWizardForm(forms.Form):
    pass

class ExpertiseWizardForm(forms.Form):
    pass

class VisibilityWizardForm(forms.Form):
    pass

class BudgetWizardForm(forms.Form):
    pass

class IndexWizardForm(forms.Form):
    pass

class ReviewWizardForm(forms.Form):
    pass