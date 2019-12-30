from django import forms
#from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from .models import CustomUser
from .choices import STATUS
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm


#class RegistrationForm(forms.ModelForm):
class RegistrationForm(UserCreationForm):
    """
    Form for registering a new user account.

    Validates that the requested username is not already in use, and
    requires the password to be entered twice to catch typos.

    Subclasses should feel free to add any additional validation they
    need, but should avoid defining a ``save()`` method -- the actual
    saving of collected user data is delegated to the active
    registration backend.
    """
    required_css_class = 'required'

    first_name = forms.CharField(max_length=100,
                                label=_("First Name"),
                                 widget=forms.TextInput(attrs={'class' : "user_form_text",
                                                               'id':'firstname',
                                                             "placeholder":"First Name",
                                                              "type":"text",
                                                              "name":"First Name"}))
    last_name = forms.CharField(max_length=100,
                                label=_("Last Name"),
                                widget=forms.TextInput(attrs={'class' : "user_form_text",
                                                              'id': 'lastname',
                                                             "placeholder":"Last Name",
                                                              "type":"text",
                                                              "name":"Last Name"}))

    username = forms.RegexField(regex=r'^[\w.@+-]+$',
                                max_length=30,
                                label=_("Username"),
                                widget=forms.TextInput(attrs={'class' : "input100 input100",
                                                              'id':'username',
                                                             "placeholder":"Username",
                                                              "type":"text",
                                                              "name":"username"}),
                                error_messages={'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters.")})

    email     = forms.CharField(widget=forms.TextInput(attrs={'class':"input100",
                                                              'id':'id_email',
                                                              "type":"email",
                                                              "name":"email",
                                                              "placeholder":"Email",
                                                              "onkeyup":"validate(input)",}),
                                label=_("email"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : "input100",'id':"psw",'name':"psw",                                                                 
                                                                'pattern':"(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}",
                                                                'title':"Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters",
                                                                  "placeholder":"**********"}),
                                label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : "input100", 'id':"psw2",'name':"psw2",                                                                 
                                                                
                                                                  "placeholder":"**********"}),
                                label=_("Password (again)"))
    # is_employer = forms.BooleanField(required=False,
    #                                   initial=False,
    #                                   label='Employer')
    #
    #
    #
    # is_jobseeker = forms.BooleanField(required=False,
    #                                   initial=False,
    #                                   label='Job Seeker')

    status = forms.CharField(widget=forms.TextInput(attrs={'type':"hidden",'name':"fname", 'id':"input", 'value':""}))

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email','id','is_jobseeker','is_employer' )

    def clean_username(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.

        """
        existing = CustomUser.objects.filter(username__iexact=self.cleaned_data['username'])
        if existing.exists():
            raise forms.ValidationError(_("A user with that username already exists."))
        else:
            return self.cleaned_data['username']

    # def clean(self):
    #     """
    #     Verifiy that the values entered into the two password fields
    #     match. Note that an error here will end up in
    #     ``non_field_errors()`` because it doesn't apply to a single
    #     field.
    #
    #     """
    #     password1 = self.cleaned_data.get('password1')
    #     if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
    #         if self.cleaned_data['password1'] != self.cleaned_data['password2']:
    #             raise forms.ValidationError(_("The two password fields didn't match."))
    #     if len(password1) < 8:
    #         raise forms.ValidationError("The new password must be at least %d characters long." % 8)
    #     return self.cleaned_data
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class EditProfileForm(UserChangeForm):
    #template_name='/something/else'

    class Meta:
        model = CustomUser
        fields = (
            'email',
            'username',
            'first_name',
            'last_name',
            'password',

            )


        widgets = {
            'email': forms.TextInput(attrs={'class':"input100",
                                                              'id':'email',
                                                              "type":"email",
                                                              "name":"email",
                                                              "placeholder":"Email",
                                                              "onkeyup":"validate(input)",}),
            'username':forms.TextInput(attrs={'class' : "input100 input100",
                                                              'id':'username',
                                                             "placeholder":"Username",
                                                              "type":"text",
                                                              "name":"username"}),

            'first_name':forms.TextInput(attrs={'class':"user_form_text", 'id':'firstname', "placeholder":"First Name","type":"text","name":"First Name"}),




            'last_name':forms.TextInput(attrs={'class' : "user_form_text",
                                                              'id': 'lastname',
                                                             "placeholder":"Last Name",
                                                              "type":"text",
                                                              "name":"Last Name"}),
            'password':forms.PasswordInput(attrs={'class' : "input100",
                                                    'id':"password1",
                                                                  "onkeyup":"validatePassword(this.value)",

                                                                  "placeholder":"**********"}),

        }


class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model =CustomUser
        fields=(
            'old_password',
            'new_password1',
            'new_password2',
        )
        widgets = {
            'old_password': forms.PasswordInput(attrs={'class':''}),
            'new_password1': forms.PasswordInput(attrs={'class': ''}),
            'new_password2': forms.PasswordInput(attrs={'class': ''}),
        }


class LoginForm(forms.Form):
    username = forms.RegexField(regex=r'^[\w.@+-]+$',
                                max_length=30,
                                label=_("Username"),
                                error_messages={'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters.")},
                                widget=forms.TextInput(attrs={'class' : "fa fa-user input100",
                                                              'id':'username',
                                                             "placeholder":"Username",
                                                              "type":"text",
                                                              "name":"username"}))



    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : "input100",
                                                                  "type":"password",
                                                                  "name":"pass",
                                                                  "placeholder":"**********"}),
                                label=_("Password"))
    #password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : "form-control"}),
     #                           label=_("Password"))

    def clean(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.

        """
        if 'username' not in self.cleaned_data and 'password1' not in self.cleaned_data:

            raise forms.ValidationError(_("please fill the forms"))
        return self.cleaned_data


