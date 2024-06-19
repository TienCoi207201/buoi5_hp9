from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Product, Post, Comment
from django.core.serializers import  serialize

# Create your views here.
# def demo(req):
#     image_path = 'images/couch.png';
#     data = [
#         {
#         'name': 'Trọng Nhân',
#         'image': 20
#     }
#     ]
#     return JsonResponse(data, safe=False)
def home(req):
    posts = Post.objects.all()
    comment = Comment.objects.all()
    image_path = 'static/images/couch.png'
    return render(req, 'pages/index.html', {'posts': posts, 'image_path': image_path, 'comments': comment})
def product(req):
    products = Product.objects.all()
    return render(req, 'pages/product.html', context={'products': products})

def show(req):
    #kiểu list: []
    data = [
        {
            'id': 1,
            'name': 'Đăng Hán',
            'born': '2003'
        },
        {
            'name': 'Văn Tiến',
            'born': '2003',
        }
    ]
    return JsonResponse(data,json_dumps_params={'ensure_ascii': False}, safe=False)

def showcomments(req):
    cmt = Comment.objects.all()
    # cmt_json = serialize('json', cmt)
    print(cmt)
    # return JsonResponse(cmt_json, json_dumps_params={'ensure_ascii': False}, safe=False)
    return render(req, 'pages/index.html', context={'comments': cmt})
def cmt_details(req, pk):
    comment = [
        {
            'id': 1,
            'name': 'comment 1',
            'image': 'https://soundpeatsvietnam.com/wp-content/uploads/2023/05/gofree.jpg'
        },
        {
            'id': 2,
            'name': 'comment 2',
            'image': 'https://cdn.tgdd.vn/Products/Images/54/310763/tai-nghe-bluetooth-true-wireless-ava-freego-a20-thumb-2-600x600.jpg'
        }
    ]
    # cmt_details = get_object_or_404(comment, pk=pk)
    return render(req, 'pages/cmt_detail.html', context={'comments': comment})
def err_404_not_found(req, exception = None):
    return render(req, 'pages/404.html', status=404)
def contact(req):
    return render(req, 'pages/contact.html')
def cart(req):
    return render(req, 'pages/cart.html')

def login_user(req):
    if req.method == "POST":
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(req, username = username, password = password)
        if user is not None:
            login(req, user)
            messages.success(req, ("You are Login!"))
            return redirect("home:home")
        else:
            messages.success(req, ("Login Failed!"))
            return redirect('home:login')
    else:
        return render(req, 'pages/login.html')

def logout_user(req):
    logout(req)
    messages.success(req, "Logout success!")
    return redirect("home:home")