from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('home', views.index, name='home'),
    path('about',views.about, name='about'),
    path('services',views.sevices, name='services'),
    path('contact', views.contact, name='contact')
]
