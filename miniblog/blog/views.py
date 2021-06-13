from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from blog.forms import SignupForm, LoginForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from blog.models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})


def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def dashboard(request):
    if request.user.is_authenticated:
       posts = Post.objects.all()
       user = request.user
       fullname = user.get_full_name()
       groups = Group.objects.all()
       return render(request, 'blog/dashboard.html', {'posts':posts, 'fullname': fullname, 'groups': groups})
    else:
       return redirect('/blog/login')

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            messages.success(request, 'You have become an Author')
            form.save()
    else:
         form = SignupForm()
    return render(request, 'blog/signup.html', {'form': form})

def user_login(request):
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
                    return redirect('/blog/dashboard')
        else:
            form = LoginForm()
        return render(request, 'blog/login.html', {'form': form})
    else:
        return redirect('/blog/dashboard')

def user_logout(request):
        logout(request)
        return redirect('/blog/login')





def addpost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Post Created Successfully')
                form.save()
                return redirect('/blog/dashboard')
        else:
            form = PostForm()
        return render(request, 'blog/addpost.html', {'form': form})
    else:
        return redirect('/login/')

def updatepost(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            p = Post.objects.get(id=id)
            form = PostForm(request.POST, instance=p)
            if form.is_valid():
                form.save()
                return redirect('/blog/dashboard')
        else:
            p = Post.objects.get(id=id)
            form = PostForm(instance=p)
        return render(request, 'blog/updatepost.html', {'form': form})
    else:
        return redirect('/login/')

def deletepost(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            p = Post.objects.get(id=id)
            p.delete
        return redirect('/blog/dashboard')
    else:
        return redirect('/login/')



# Create your views here.
