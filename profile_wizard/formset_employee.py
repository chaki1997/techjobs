from django import forms
from .choices import \
    LENGUAGE_CHOICES,\
    YEAR_FROM,\
    YEAR_TO,\
    ROLE,\
    AVAILABILITY,\
    STATUS,\
    OPTION,\
    DEGREE,\
    MONTH

from .category import CATEGORY

from .models import \
    EmployeeProfileModel,\
    EmloymentWizard,\
    EduWizard
from django.forms import ModelForm

class EmployeeEditForm(ModelForm):
    status = forms.ChoiceField(choices=OPTION, required=False,
                               widget=forms.Select(attrs={'name': "", 'id': "", 'style': "width:30%;"}))

    prof_title = forms.CharField(label='Title',
                                 widget=forms.TextInput(attrs={'onclick': "add(id)", 'class': 'C#_developer',
                                                               'placeholder': "Example: Backend Developer"}))

    prof_overview = forms.CharField(required=False,
                                    widget=forms.Textarea(attrs={'onclick': "add(id)", "rows": 10, "cols": 60,
                                                                 "placeholder": "Highlight your top skills, experience, and interests. "
                                                                                "This is one of the things employers "
                                                                                "will see in your profile ",
                                                                 "id": 'text_area',
                                                                 "name": 'textarea'
                                                                 }))


    #HOUR_RATE

    availability = forms.ChoiceField(choices=AVAILABILITY, label="",
                                     widget=forms.Select(attrs={"class": 'select_profiction'}))
    paymant = forms.IntegerField(widget=forms.TextInput(
        attrs={'class': 'input_price', 'placeholder': '0.00', 'onchange': "vatCalculation()", 'id': "subtotal"}))

    #PROFICIANCY

    language_compatancy = forms.ChoiceField(choices=LENGUAGE_CHOICES, label="",
                                            widget=forms.Select(attrs={"class": 'select_profiction'}))
    category_industry = forms.ChoiceField(choices=CATEGORY, widget=forms.Select(attrs={'class': 'select_category'}))

    #LOCATION

    address_1 = forms.CharField(required=False, max_length=128,
                                widget=forms.TextInput(attrs={'type': 'text', 'name': 'address_1'}))
    #address_2 = forms.CharField(required=False, max_length=128,
    #                            widget=forms.TextInput(attrs={'type': 'text', 'name': 'address_2'}))
    city = forms.CharField(required=False, max_length=64, widget=forms.TextInput(
        attrs={'type': 'text', 'name': 'city', 'placeholder': 'start typing your city'}))
    zip_code = forms.CharField(required=False, max_length=5, widget=forms.TextInput(
        attrs={'class': 'postal_input', 'type': 'text', 'name': 'Postal Code'}))
    country = forms.CharField(required=False, max_length=128, widget=forms.TextInput(
       attrs={'class': 'select_input_1', 'type': 'text', 'name': 'Country', 'placeholder': 'Country'}))
    phone = forms.IntegerField(widget=forms.TextInput(attrs={'id': 'phonenumebr'}))
    #phone_number = PhoneNumberField(required=False, widget=forms.TextInput(attrs={'id': 'phonenumebr'}))
    class Meta:
        model = EmployeeProfileModel
        fields = ('status','prof_title','prof_overview','language_compatancy',
            'category_industry',
               'address_1','city','zip_code','country')
        exclude = ('user','address_2')

class EducationEditForm(ModelForm):
    school = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'first', 'style': 'display:block', 'class': 'first_scenario', 'id': 'input_school', }))


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

    area_of_study = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'first_scenario', 'type': 'text', 'name': 'Area_of_study', 'id': 'Area_of_study'}))
    Description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={'class': 'first_scenario', 'name': 'Description', 'id': 'input_desctiption', 'cols': '69',
               'rows': '10'}))



    class Meta:
        model = EduWizard
        fields = ('school','started','ended','degree','area_of_study','Description',)
        exclude = []

from django.forms.models import inlineformset_factory
EducationFormSet = inlineformset_factory(EmployeeProfileModel, EduWizard,
                                            form=EducationEditForm, fields = ('school','started','ended','degree','area_of_study','Description'),exclude=('profile','id',''),can_order=False,extra=0,can_delete=False)




class EmplymentEditForm(ModelForm):

    company = forms.CharField(widget=forms.TextInput(attrs={'type':'text','name':'company','id':'input_Company'}))
    title = forms.CharField(required=False,widget=forms.TextInput(attrs={'type':'text','name':'input_degree','id':'input_degree_2'}))
    location = forms.CharField(required=False,widget=forms.TextInput(attrs={'type':'text','placeholder':'City','id':'Location_input'}))
    country = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'type': 'text', 'placeholder': 'country', 'id': 'monitor_country'}))
    role =  forms.ChoiceField(required=False,choices=CATEGORY, widget=forms.Select(attrs={'id':'select_Role'}))
    period_sterted = forms.ChoiceField(required=False,choices=YEAR_FROM,widget=forms.Select(attrs={'id':'select_Role_month','class':'col-md-5 offset-1'}))
    month_started = forms.ChoiceField(required=False, choices=MONTH, widget=forms.Select(
        attrs={'id': 'from_month', 'class': 'col-md-5 offset-1'}))
    period_ended = forms.ChoiceField(required=False,choices=YEAR_TO,widget=forms.Select(attrs={'id':'select_Role_month','class':'col-md-5 offset-1'}))
    month_ended = forms.ChoiceField(required=False, choices=MONTH, widget=forms.Select(
        attrs={'id': 'to_month', 'class': 'col-md-5 offset-1'}))
    is_current = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'type':'checkbox'}))
    description = forms.CharField(required=False,widget=forms.Textarea(attrs={'class':'first_scenario','name':'Description','id':'input_desctiption','cols':'69','rows':'10'}))


    class Meta:
        model = EmloymentWizard
        fields = ('company','title','location','country','role','period_sterted','month_started','period_ended','month_ended','is_current','description')
        exclude = []

EmploymentFormSet = inlineformset_factory(EmployeeProfileModel, EmloymentWizard,form=EmplymentEditForm, fields=('company','location', 'title',  'country','role', 'period_sterted','month_started', 'period_ended','month_ended', 'is_current', 'description'), extra=0)

