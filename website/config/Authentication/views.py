from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout

# Create your views here.


def signout(request):
    logout(request)
    return redirect('HomeApp:index')

