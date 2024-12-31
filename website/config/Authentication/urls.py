from django.urls import path
from .views import *

urlpatterns = [
    path('signout/', signout, name='signout'),

]