from django.urls import path, re_path
from . import views
app_name = 'home'
urlpatterns = [
    path('user', views.demo, name = 'demo'),
    path('home', views.home, name = 'home'),
    path('product', views.product, name='product'),
    path('comment', views.showcomments, name = 'comments'),
    path('comment-detail/<int:pk>', views.cmt_details, name = 'comment-detail'),
    path('contact', views.contact, name = 'contact'),
    path('cart', views.cart, name = 'cart'),
    path('demo', views.demo, name = 'demo'),
    path('notfound', views.err_404_not_found, name = 'not_found'),
    # re_path(r'^.*$', views.err_404_not_found),
]