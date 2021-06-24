from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User

from myapp.models import Patient, PatientCureHistory


class SignupForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'firs_name': 'First Name', 'last_name': 'Last Name'}
        error_messages = {
            'username': {'required': 'First Name is Required'},
        }
        widgets = {

            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }

class LoginForm(AuthenticationForm):
  username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
  password = forms.CharField(label="Password", strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password',
                       'class': 'form-control'}))


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        labels = {'date_of_birth': 'Date Of Birth'}

        widgets = {
              'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entern Patient Name'}),
              'father_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Father Name'}),
              'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Mobile Number'}),
              'date_of_birth': forms.DateInput(attrs={'type':'date','class': 'form-control', 'placeholder': 'Enter Date of Birth'})
           }

class PatientHistoryForm(forms.ModelForm):
    class Meta:
        model = PatientCureHistory
        fields = '__all__'
        labels = {'cure_date': 'Cure Date'}
       # patient = models.ForeignKey(Patient, on_delete=models.PROTECT)

        widgets = {
              'disease': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entern Disease'}),
              'cure': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Cure Detail'}),
              #'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Mobile Number'}),
              'cure_date': forms.DateInput(attrs={'type':'date','class': 'form-control', 'placeholder': 'Enter Cure Date'})
           }


