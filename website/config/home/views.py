from django.shortcuts import redirect, render
from .models import * 
from .forms import *
from django.http import FileResponse
from django.shortcuts import get_object_or_404
import os
from django.core.paginator import Paginator


def download_file(request, file_id):
    # پیدا کردن فایل از روی id یا هر پارامتر دیگر
    file_path = get_object_or_404(LegalFiles, id=file_id).file.path  # فرض کنید فیلد file در مدل وجود دارد
    
    # بررسی وجود فایل
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=os.path.basename(file_path))
    else:
        from django.http import Http404
        raise Http404("File not found.")

def index(request):
    legalfiles = LegalFiles.objects.all()
    lawyertp = Lawyer.objects.all()
<<<<<<< HEAD
    lawyers = Lawyer.objects.all().order_by('-date')[:4]
    context = {
        'lawyers': lawyers,
    }
    return render (request ,"home/index.html",context)
=======
    sm = SabtMoshavereForm()
    if request.method == 'POST':
        if 'sm' in request.POST:
            sm = SabtMoshavereForm(request.POST)
            print('yeeeeeeeeeeeeeeeeee')
            if sm.is_valid():
                instance = sm.save(False)
                instance.profile = request.user.profile
                instance.save()
                sm = SabtMoshavereForm()
                return redirect('HomeApp:index')
    return render(request ,"home/index.html",{'sm':sm})
>>>>>>> 7486fb3904f70cfb3b83ee512e0a8fd4191d733d

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


def detailvakil(request, lk):
    lawyer = get_object_or_404(Lawyer, id=lk)
    return render(request, "home/DetailsVakil.html", {'lawyer': lawyer})
def lawyers_list(request):
    lawyers = Lawyer.objects.all()
    paginator = Paginator(lawyers, 6)  # تعداد وکلا در هر صفحه
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home/lawyers_list.html', {'page_obj': page_obj})
