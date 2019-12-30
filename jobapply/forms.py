from django import forms
from . import models


class JobAbblyForm(forms.ModelForm):
    coverletter = forms.CharField(required=False,
                                    widget=forms.Textarea(attrs={"rows": 10, "cols": 60,

                                                                 "id": 'text_area',
                                                                 "name": 'textarea', 'placeholder':'Why should you be hired?',
                                                                 }))

    class Meta:
        model = models.JobApply
        fields = ('coverletter', )