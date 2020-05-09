from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"), 
    path('viewurls', views.view_url, name= "view_url"),
    path('saveurls', views.save_url, name = "save_url"),
    path('newurl', views.new_url, name="new_url"),
    
    
]