from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Product, Post

# Create your views here.
def demo(req):
    image_path = 'images/couch.png';
    data = [
        {
        'name': 'Trọng Nhân',
        'image': 20
    }
    ]
    return JsonResponse(data, safe=False)
def home(req):
    posts = Post.objects.all()
    image_path = 'static/images/couch.png'
    return render(req, 'pages/index.html', {'posts': posts, 'image_path': image_path})
def product(req):
    data = [
        {
            'name': 'Đăng Hán',
            'born': '2003'
        },
        {
            'name': 'Văn Tiến',
            'born': '2003',
        }
    ]
    return render(req, 'pages/product.html', {'products': data})

def show(req):
    #kiểu list: []
    data = [
        {
            'name': 'Đăng Hán',
            'born': '2003'
        },
        {
            'name': 'Văn Tiến',
            'born': '2003',
        }
    ]
    return JsonResponse(data,json_dumps_params={'ensure_ascii': False}, safe=False)