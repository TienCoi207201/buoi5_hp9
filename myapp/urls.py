from django.urls import path, re_path
from . import views

from .views import HomeListView, ProductListView, CommentListView
app_name = 'home'

urlpatterns = [
    # path('user', views.demo, name = 'demo'),
    path('home', HomeListView.as_view(), name = 'home'),
    path('login', views.login_user, name = 'login'),
    path('logout', views.logout_user, name = 'logout'),
    path('signup', views.signup_user, name = 'signup'),
    path('product', ProductListView.as_view(), name='product'),
    path('comment', CommentListView.as_view(), name = 'comments'),
    path('comment-detail/<int:pk>', views.cmt_details, name = 'comment-detail'),
    path('contact', views.contact, name = 'contact'),
    path('cart', views.cart, name = 'cart'),
    path('showdata', views.showData, name = 'show'),
    path('product/view', views.viewProduct, name = 'view_product'),
    path('product/edit/<int:pk>', views.editProduct, name = 'edit_product'),
    path('product/delete/<int:pk>', views.deleteProduct, name = 'delete_product'),
    path('', views.showData, name = 'show'),
    path('showdata', views.showData, name = 'show'),
    path('product-return', views.produduct_req, name = 'product_req'),
    path('filter-product', views.filterProduct, name = 'filter_product'),
    re_path(r'^.*$', views.err_404_not_found),
]