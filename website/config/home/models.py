from django.db import models
from Authentication.models import Profile
from ckeditor.fields import RichTextField


class LawyerType(models.Model): 
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name  
        
class Lawyer(models.Model):
    lawyer_type = models.ForeignKey(LawyerType,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    experience = RichTextField()
    date = models.DateField()
    image = models.ImageField(upload_to='lawyer_images')

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
    def __str__(self):
        return self.full_name

class BillRequest(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    file = models.FileField(upload_to='bill_requests')

    def __str__(self):
        return self.username
    
class News(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="news_images")
    title = models.CharField(max_length=100)
    content = RichTextField()
    date = models.DateField(auto_now_add=True)

class LegalCategory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class LegalFiles(models.Model):
    category = models.ForeignKey(LegalCategory, on_delete=models.CASCADE)
    file = models.FileField(upload_to='legal_files')
    def __str__(self):
        return self.file.name