from django.urls import path
from . import views

app_name = "HomeApp"
urlpatterns = [
    path('', views.index , name="index"),
    path('about/', views.about , name="about"),
    path('faq/', views.faq , name="faq"),
    path('contact/', views.contact , name="contact"),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
    path('vakil_profile/' , views.vakil_profile , name="vakil_profile"),
    path('detailvakil/<int:lk>/', views.detailvakil, name='detailvakil'),
    path('lawyers_list/', views.lawyers_list, name="lawyers_list"), 
# <<<<<<< HEAD
    path('DadKhastNevisi/', views.DadKhastNevisi, name="DadKhastNevisi"), 
# =======
    path('sabt_moshaver/',views.sabt_moshaver,name='sabt_moshaver')
<<<<<<< HEAD
]
=======
# >>>>>>> 356bddf320320a201149e1fbf31bdc58944969e3
]

>>>>>>> ccc9f6f5627e884f80dfda677af78252851dd4a1
