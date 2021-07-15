from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        labels = {'firs_name': 'First Name', 'last_name':'Last Name'}

        error_messages = {
            'first_name': {'required': 'First Name is Required'},
            'last_name': {'required': 'Last Name is Required'},
            'email': {'required': 'Email is Required'},
            'phone': {'required': 'Mobile number is Required'},
            'password': {'required': 'Password is Required'},
        }
        widgets = {

            'phone': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Enter Mobile Number'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Enter Email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Enter Email'}),
            #### date picker show krny k liye   'type':'date'
        }

    def clean(self):
        cleaned_data = super().clean()
        email = self.cleaned_data.get('email')
        if Customer.objects.filter(email=email):
            print(Customer.objects.filter(email=email))
            #raise forms.ValidationError({"email": "user already exist with this email"})
            raise forms.ValidationError( "user already exist with this email")

class LoginForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['email', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Enter Email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Enter Password'})
        }

        error_messages = {
            'password': {'required': 'Password is Required'},
            'email': {'required': 'Email is Required'},
        }


