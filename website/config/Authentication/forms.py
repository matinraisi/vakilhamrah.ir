from django import forms

class Signup(forms.Form):
    username = forms.CharField(max_length=100,widget=forms.TextInput({'class':'form-control text-left','placeholder':'نام کاربری'}))
    phone_number = forms.CharField(max_length=20,widget=forms.TextInput({'class':'form-control text-left','placeholder':'شماره تماس'}))
    email = forms.EmailField(widget=forms.EmailInput({'class':'form-control text-left','placeholder':'ایمیل'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput({'class':'form-control text-left','placeholder':'رمز ورود'}))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput({'class':'form-control text-left','placeholder':'تکرار رمز ورود'}))

class Login(forms.Form):
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'id':'singin-email','name':'singin-email','class':'form-control text-left','placeholder': 'نام کاربری یا ایمیل'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'id':'singin-password','name':'singin-password','class':'form-control text-left ltr','placeholder': 'رمز عبور'}))

