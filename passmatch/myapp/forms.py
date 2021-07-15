from django import forms
from .models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def clean(self):
        cleaned_data = super()
        val1 = self.cleaned_data.get('namee')
        val2 = self.cleaned_data.get('name1')
        if val1 != val2:
            raise forms.ValidationError('password not matched Mudassir')
