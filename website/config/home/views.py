from django.shortcuts import redirect, render

from .models import * 
from .forms import *
# Create your views here.

def index(request):
    
    return render (request ,"home/index.html")
def contact(request):
    form = ContactUsForm()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('HomeApp:contact')

    return render (request ,"home/contact-us.html",{'form':form})
def faq(request):
    form = QaAForm()
    if request.method == 'POST':
        
        form = QaAForm(request.POST)
        if form.is_valid():
            qaainstance = form.save(commit=False)
            qaainstance.profile = request.user.profile
            qaainstance.save()
            form = QaAForm()
            redirect('HomeApp:faq')
            
    return render (request ,"home/faq.html",{'form':form})
def about(request):
    return render (request ,"home/about-us.html")