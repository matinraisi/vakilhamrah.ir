from django.urls import path
from . import views

app_name = "HomeApp"
urlpatterns = [
    path('', views.index , name="index"),
    path('about/', views.about , name="about"),
    path('faq/', views.faq , name="faq"),
    path('contact/', views.contact , name="contact"),
    path('details/', views.detailvakil , name="details"),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
]

