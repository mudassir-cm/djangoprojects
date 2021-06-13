from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from blog.models import Post

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

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        labels = {'desc': 'Description'}

        widgets = {
              'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Title'}),
              'desc': forms.Textarea(attrs={'rows':3, 'class': 'form-control', 'placeholder': 'Enter Description'})
           }