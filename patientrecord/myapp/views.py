from django.contrib import messages
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from myapp.forms import SignupForm, LoginForm, PatientForm, PatientHistoryForm
from django.contrib.auth import login, logout, authenticate

from myapp.models import Patient, PatientCureHistory


def home(request):
    return render(request, 'myapp/home.html')

def usersignup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            messages.success(request, 'You have become an Authorized doctor on Doctor Alia Click')
            form.save()
    else:
        form = SignupForm()
    return render(request, 'myapp/signup.html', {'form': form})

def userlogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'login successfully')
                    return redirect('/myapp/dashboard')
        else:
            form = LoginForm()
        return render(request, 'myapp/login.html', {'form': form})
    else:
        return redirect('/myapp/dashboard')


def userlogout(request):
    logout(request)
    return redirect('/myapp/userlogin')


def dashboard(request):
    if request.user.is_authenticated:
        patients = Patient.objects.all()
        user = request.user
        fullname = user.get_full_name()
        groups = Group.objects.all()
        ip = request.session.get('ip', 0)

        return render(request, 'myapp/dashboard.html',
                      {'patients': patients, 'fullname': fullname, 'groups': groups, 'ip': ip})
    else:
        return redirect('/myapp/login')

def addpatient(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PatientForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Patient Created Successfully')
                form.save()
                return redirect('/myapp/dashboard')
        else:
            form = PatientForm()
        return render(request, 'myapp/addpatient.html', {'form': form})
    else:
        return redirect('/login/')

def updatepatient(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            p = Patient.objects.get(id=id)
            form = PatientForm(request.POST, instance=p)
            if form.is_valid():
                form.save()
                return redirect('/myapp/dashboard')
        else:
            p = Patient.objects.get(id=id)
            form = PatientForm(instance=p)
        return render(request, 'myapp/updatepatient.html', {'form': form})
    else:
        return redirect('/login/')

def deletepatient(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            p = Patient.objects.get(id=id)
            p.delete()
        return redirect('/myapp/dashboard')
    else:
        return redirect('/login/')


def patienthistory(request, id):
    if request.user.is_authenticated:
        patient = Patient.objects.get(id = id)
        return render(request, 'myapp/patienthistory.html',
                      {'patient': patient})
    else:
        return redirect('/myapp/login')

def addpatienthistory(request, id):
    if request.user.is_authenticated:
        patient = Patient.objects.get(id = id)
        if request.method == 'POST':
            form = PatientHistoryForm(request.POST)
            if form.is_valid():
                messages.success(request, ' cure history added %s successfully' % patient.name)
                form.save()
                return redirect('patienthistory', id=id)
                #return redirect(reverse('/myapp/patienthistory', kwargs={"user_id": id}))
        else:
            form = PatientHistoryForm()
        return render(request, 'myapp/addpatienthistory.html', {'form': form})
    else:
        return redirect('/login/')

def updatepatienthistory(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            p = PatientCureHistory.objects.get(id=id)
            form = PatientHistoryForm(request.POST, instance=p)
            if form.is_valid():
                form.save()
                patient = Patient.objects.get(patientcurehistory__id = id)
                return redirect('patienthistory', id = patient.id)
        else:
            p = PatientCureHistory.objects.get(id=id)
            form = PatientHistoryForm(instance=p)
        return render(request, 'myapp/updatepatienthistory.html', {'form': form})
    else:
        return redirect('/login/')

def deletepatienthistory(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            p = PatientCureHistory.objects.get(id=id)

            p.delete()
            patient = Patient.objects.get(patientcurehistory__id = id)
           # print(patient.id)
        return redirect('patienthistory', id = patient.id)
       # return redirect('employee/view', id=id)
    else:
        return redirect('/login/')


# Create your views here.
