
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('', views.home ,name='home'),
    path('ro/', views.home ,name='home'),
    path('ro/about/', views.about ,name='about'),
    path('ro/home/', views.home ,name='home'),
    path('ro/platform/', views.platform ,name='platform'),
    path('ro/faqs/', views.faqs ,name='faqs'),
    path('ro/cookie/', views.cookie ,name='cookie'),
    path('ro/webapp/', views.webapp ,name='webapp'),
    path('ro/contact/', views.contact ,name='contact'),

]
