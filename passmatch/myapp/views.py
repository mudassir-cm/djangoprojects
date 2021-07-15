from django.shortcuts import render
from myapp.forms import PersonForm

def home(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
             pass
        else:
            return render(request, 'myapp/home.html', {'form': form})
    else:
        form = PersonForm()
    return render(request, 'myapp/home.html', {'form': form})
# Create your views here.
