from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(max_length=10, error_messages={'max_length':'max'}, empty_value='kkk')
    age = forms.IntegerField(min_value=12, max_value=18,
                             error_messages={
                                 'required':'ye chaye he',
                                 'min_value':'ye 12 se bara ya brabar hona chye',
                                 'max_value':'18 se chota ya braber hona chaye',
                                 'invalid':'invalid'
                             }, initial=13)
    agree = forms.BooleanField(error_messages={'required':'kkkkk'})
    price = forms.DecimalField(min_value=5, max_value=10, max_digits=4, decimal_places=1,
    error_messages = {
        'required': 'ye chaye he',
        'min_value': '5 k brabr ya greater ho',
        'max_value': '10 k brabr ya less than ho',
        'max_digits': 'zada se zada 4 digits hon',
        'max_decimal_places': '1 hony chaye',
        'invalid':'invalid numver',

    })