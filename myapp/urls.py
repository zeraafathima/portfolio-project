from django.contrib import admin
from django.urls import path
from . import views  # Import your views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact_view, name='contact'),
    path('skills/', views.skills, name='skills'),
    path('resume/', views.resume, name='resume'),
    path('services/', views.services, name='services'),
]
