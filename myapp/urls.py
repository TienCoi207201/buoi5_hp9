from django.urls import path
from . import views

urlpatterns = [
    path('user', views.demo, name = 'demo'),
    path('home', views.home, name = 'home'),
    path('product', views.product, name='product'),
    path('show', views.show, name = 'show')
]