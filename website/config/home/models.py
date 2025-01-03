from django.db import models
from Authentication.models import Profile
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField

class LawyerType(models.Model): 
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name  
        
class Lawyer (models.Model):
    lawyer_type = models.ForeignKey(LawyerType,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    experience = RichTextField()
# <<<<<<< HEAD
    date = models.DateField()
    image = ResizedImageField(upload_to='lawyer_images' , crop=['middle', 'center'] , size=[300,300],quality=75)
# # =======
#     date = models.DateTimeField(auto_now_add=True)
#     image = models.ImageField(upload_to='lawyer_images')
# >>>>>>> 7486fb3904f70cfb3b83ee512e0a8fd4191d733d

    def __str__(self):
        return self.name

 

class QaA(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    sb_types = (
        ('fa', 'خانوادگی'),
        ('ju', 'قضایی'),
        ('ma', 'مدنی'),
        ('je', 'جنایی'),
        ('ot', 'سایر'),)

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    is_read = models.BooleanField(default=False,blank=False)
    subject_type = models.CharField(max_length=100, choices=sb_types)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.full_name} - {self.message[0:12]}'
    

class ContactUs(models.Model):
    full_name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.full_name
    
class DadKhastCaregory(models.Model):
    type = models.CharField(max_length=20)
    def __str__(self):
        return self.type

class DadKhastNevisi(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    subject_type = models.ForeignKey(DadKhastCaregory,models.CASCADE)
    title = models.CharField(max_length=40)
    subject = models.CharField(max_length=50)
    file = models.FileField(upload_to='dadkhast_request')
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
class SabtMoshavere(models.Model):
    profile = models.ForeignKey(Profile,models.CASCADE)
    phone_number = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.phone_number)
    
class News(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="news_images")
    title = models.CharField(max_length=100)
    content = RichTextField()
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title

class LegalCategory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class LegalFiles(models.Model):
    category = models.ForeignKey(LegalCategory, on_delete=models.CASCADE)
    file = models.FileField(upload_to='legal_files')
    def __str__(self):
        return self.file.name