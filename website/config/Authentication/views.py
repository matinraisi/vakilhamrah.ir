from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.dispatch import receiver
from django.db.models.signals import post_save
from .forms import *
from .models import *

# Create your views here.


def signout(request):
    logout(request)
    return redirect('HomeApp:index')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(instance, **kwargs):
    if not hasattr(instance, 'profile'):
        # Create the profile if it doesn't exist
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()

users_without_profiles = User.objects.filter(profile__isnull=True)

# اگه دیتا بیس رو حذف کنی باید برای این که میگریت کنی این دو تا خط رو حذف کنی
for user in users_without_profiles:
    Profile.objects.create(user=user)