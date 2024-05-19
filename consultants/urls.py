from django.urls import path

from . import views

urlpatterns = [
    path('', views.consultants, name='consultants'),    
   
]
