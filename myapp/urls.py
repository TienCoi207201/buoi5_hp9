from django.urls import path, re_path
from . import views
app_name = 'home'
urlpatterns = [
    # path('user', views.demo, name = 'demo'),
    path('home', views.home, name = 'home'),
    path('login', views.login_user, name = 'login'),
    path('logout', views.logout_user, name = 'logout'),
    path('product', views.product, name='product'),
    path('comment', views.showcomments, name = 'comments'),
    path('comment-detail/<int:pk>', views.cmt_details, name = 'comment-detail'),
    path('contact', views.contact, name = 'contact'),
    path('cart', views.cart, name = 'cart'),
    re_path(r'^.*$', views.err_404_not_found),
]