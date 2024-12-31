from django.db import models
from django.contrib.auth.models import User
from Authentication.models import *



    
class Lawyer(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    experience = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='lawyer_images')
    sb_types = (
        ('fa', 'خانوادگی'),
        ('ju', 'قضایی'),
        ('ma', 'مدنی'),
        ('je', 'جنایی'),)
    subject_type = models.CharField(max_length=100, choices=sb_types)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    sb_types = (
        ('fa', 'خانوادگی'),
        ('ju', 'قضایی'),
        ('ma', 'مدنی'),
        ('je', 'جنایی'),)

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    subject_type = models.CharField(max_length=100, choices=sb_types)
    date = models.DateField()

    def __str__(self):
        return self.name
    

class BillRequest(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    file = models.FileField(upload_to='bill_requests')

    def __str__(self):
        return self.username
    
