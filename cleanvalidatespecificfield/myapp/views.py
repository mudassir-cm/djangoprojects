from django.shortcuts import render
from .forms import StudentForm

def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            print('Age:', age)
    else:
        form = StudentForm()
    return render(request, 'myapp/home.html', {'form': form})

# Create your views here.
