from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(initial = 'Mudasir', widget=forms.TextInput(attrs={'class':'form-control form-control-sm', 'id':'uniqueid'}) )
    email = forms.EmailField(label = 'Your Email', label_suffix = ' ',widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm'}))
    city = forms.CharField(disabled = True, widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    father_name = forms.CharField(help_text = 'is me sirf 10 char likhy ja skty hen', required=False,
                                  widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}))
    roll_num = forms.CharField(widget = forms.NumberInput(attrs={'class':'form-control form-control-sm'}), label='Roll Number')
    abc = forms.CharField(widget = forms.HiddenInput(attrs={'class':'form-control form-control-sm'}))
    date = forms.CharField(widget = forms.DateInput(attrs={'class':'form-control form-control-sm'}))
    date_time = forms.CharField(widget = forms.DateTimeInput(attrs={'class':'form-control form-control-sm'}))
    time = forms.CharField(widget = forms.TimeInput(attrs={'class':'form-control form-control-sm'}))
    text_area = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control form-control-sm'}))
    check_box = forms.CharField(widget = forms.CheckboxInput(attrs={'class':'form-check-input'}))
    file = forms.CharField(widget = forms.FileInput(attrs={'class':'form-control-file'}))























