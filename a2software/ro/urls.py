
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('', views.home ,name='home'),
    path('ro/', views.home ,name='home'),
    path('ro/about/', views.about ,name='about'),
     path('ro/home/', views.home ,name='home'),

]
