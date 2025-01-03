from django import forms
from .models import *

class QaAForm(forms.ModelForm):
    class Meta:
        model = QaA
        fields = ['full_name','email','subject_type','subject','is_read','message']
        widgets = {
            'full_name':forms.TextInput(attrs={'class':'form-control text-left ltr','placeholder':'نام و نام خانوادگی'}),
            'email':forms.EmailInput(attrs={'class':'form-control text-left','placeholder':'ایمیل'}),
            'subject':forms.TextInput({'class':'form-control text-left ltr','placeholder':'موضوع'}),
            'message':forms.Textarea(attrs={'class':'form-control mb-4','placeholder':'سوال'}),
            'is_read':forms.CheckboxInput(attrs={'class':'custom-checkbox','type':'checkbox','id':'register-agree'}),
            'subject_type':forms.Select(attrs={'class':'form-control','placeholder':'type'}),
        }

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'
        widgets = {
            'full_name':forms.TextInput(attrs={'class':'form-control text-left ltr','placeholder':'نام و نام خانوادگی'}),
            'email':forms.EmailInput(attrs={'class':'form-control text-left','placeholder':'ایمیل'}),
            'message':forms.Textarea(attrs={'class':'form-control mb-4','placeholder':'سوال'}),
        }

class DadkhastNevisiForm(forms.ModelForm):
    class Meta:
        model = DadKhastNevisi
        fields = ['subject_type','title','subject','file']
        widgets = {
            'subject_type':forms.Select()
        }

class SabtMoshavereForm(forms.ModelForm):
    class Meta:
        model = SabtMoshavere
        fields = ['phone_number']
        widgets = {
            'phone_number':forms.NumberInput(attrs={'class':'form-control form-solid text-left','placeholder':'شماره موبایل '})
        }