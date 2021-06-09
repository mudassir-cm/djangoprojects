from django import forms

class StudentForm(forms.Form):
    age = forms.IntegerField(help_text='Enter age between 12 and 18')

    def clean_age(self):
        ageval = self.cleaned_data['age']
        if ageval>=12 and ageval<=18:
            return ageval
        else:
            raise forms.ValidationError('should be between 12 and 18')