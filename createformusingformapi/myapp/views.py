from django.shortcuts import render
from .forms import StudentForm

def home(request):
    form = StudentForm
    return render(request, 'myapp/home.html', {'form':form})

# Create your views here.
