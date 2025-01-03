from django.urls import path
from . import views

app_name = "HomeApp"
urlpatterns = [
    path('', views.index , name="index"),
    path('about/', views.about , name="about"),
    path('faq/', views.faq , name="faq"),
    path('contact/', views.contact , name="contact"),
    # path('details/', views.detailvakil , name="details"),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
    path('vakil_profile/' , views.vakil_profile , name="vakil_profile"),
    # path('all_vakill/' , views.all_vakill , name="all_vakill"),
    path('detailvakil/<int:lk>/', views.detailvakil, name='detailvakil'),
    path('lawyers_list/', views.lawyers_list, name="lawyers_list"), 
    path('sabt_moshaver/',views.sabt_moshaver,name='sabt_moshaver')
]

