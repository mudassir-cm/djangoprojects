from django.shortcuts import render
from myapp.forms import StudentForm

def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            print(name)
    else:
        form = StudentForm()
    return render(request, 'myapp/home.html', {'form': form})

# Create your views here.
