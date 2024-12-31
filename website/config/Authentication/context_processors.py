from django.shortcuts import render
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout

# Create your views here.
def signup(request):
    form = Signup()
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['password'] == cd['password2']:
                if User.objects.filter(username=cd['username']).exists():
                    return {'form': form, 'errors': 'Username already exists'}
                    
                else:
                    User.objects.create_user(cd['username'], cd['email'], cd['password'])
                    form = Signup()
                    return {'signup': form, 'success': 'User created successfully'}
            else:
                form = Signup()
                return {'form': form, 'errors': 'Passwords do not match'}
    form = Signup()
    return {'signup': form,}
            

def signin(request):
    form = Login()
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password']) if cd['username'] and cd['password'] else authenticate(email=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                form = Login()
                return {'signin': form, 'success': 'User logged in successfully'}
            else:
                form = Login()
                return {'signin': form, 'errors': 'Invalid credentials'}
    form = Login()
    return {'signin': form}


