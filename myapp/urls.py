from django.urls import path
from . import views

urlpatterns = [
    path('user', views.demo, name = 'demo'),
    path('home', views.home, name = 'home')
]