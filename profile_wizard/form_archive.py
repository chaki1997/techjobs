'''
class ProfileForm2(forms.Form):
    school = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'first','style': 'display:block','class':'first_scenario','id':'input_school',}))
    started = forms.ChoiceField(choices = YEAR_FROM, label="",  widget=forms.Select(attrs={'class':'first_scenario','id':'input_select_form','placeholder':'FROM','lable':'asdasd'}))
    ended = forms.ChoiceField(choices = YEAR_TO, label="",  widget=forms.Select(attrs={'class':'first_scenario','id':'input_select_form_2'}))
    degree = forms.CharField(widget=forms.TextInput(attrs={'class':'first_scenario','id':'input_degree','type':'text' , 'name':'input_degree',}))
    area_of_study =  forms.CharField(widget=forms.TextInput(attrs={'class':'first_scenario','type':'text','name':'Area_of_study','id':'Area_of_study'}))
    Description = forms.CharField(widget=forms.Textarea(attrs={'class':'first_scenario','name':'Description','id':'input_desctiption','cols':'69','rows':'10'}))


    school_second = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'second','style': 'display:block','class':'second_scenario','id':'input_school',}))
    started_second = forms.ChoiceField(choices = YEAR_FROM, label="",  widget=forms.Select(attrs={'class':'second_scenario','id':'input_select_form','placeholder':'FROM','lable':'asdasd'}))
    ended_second = forms.ChoiceField(choices = YEAR_TO, label="",  widget=forms.Select(attrs={'class':'second_scenario','id':'input_select_form_2'}))
    degree_second = forms.CharField(widget=forms.TextInput(attrs={'class':'second_scenario','id':'input_degree','type':'text' , 'name':'input_degree',}))
    area_of_study_second =  forms.CharField(widget=forms.TextInput(attrs={'class':'second_scenario','type':'text','name':'Area_of_study','id':'Area_of_study'}))
    Description_second = forms.CharField(widget=forms.Textarea(attrs={'class':'second_scenario','name':'Description','id':'input_desctiption','cols':'69','rows':'10'}))
    repeat = forms.BooleanField(required=False)
    class Meta:
        model = EducationWizard
        fields = ('repeat','school','started','ended','degree','area_of_study','Description','school_second','started_second','ended_second','degree_second','area_of_study_second','Description_second' )
'''

'''
class EducationForm(forms.Form):
    school = forms.CharField(widget=forms.TextInput(attrs={'id':'input_school','class':'first_scenario'}))
    started = forms.ChoiceField(choices = YEAR_FROM, label="",  widget=forms.Select(attrs={'class':'first_scenario','id':'input_select_form','placeholder':'FROM','lable':'asdasd'}))
    ended = forms.ChoiceField(choices = YEAR_TO, label="",  widget=forms.Select(attrs={'class':'first_scenario','id':'input_select_form_2'}))
    degree = forms.CharField(widget=forms.TextInput(attrs={'class':'first_scenario','id':'input_degree','type':'text' , 'name':'input_degree',}))
    area_of_study =  forms.CharField(widget=forms.TextInput(attrs={'class':'first_scenario','type':'text','name':'Area_of_study','id':'Area_of_study'}))
    Description = forms.CharField(widget=forms.Textarea(attrs={'class':'first_scenario','name':'Description','id':'input_desctiption','cols':'69','rows':'10'}))

    class Meta:
        model = EduWizard
'''
