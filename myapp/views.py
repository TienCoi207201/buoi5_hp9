from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from .models import Product, Post, Comment
from django.core.serializers import  serialize

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
    products = Product.objects.all()
    return render(req, 'pages/product.html', context={'products': products})

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

def showcomments(req):
    cmt = Comment.objects.all()
    # cmt_json = serialize('json', cmt)
    print(cmt)
    # return JsonResponse(cmt_json, json_dumps_params={'ensure_ascii': False}, safe=False)
    return render(req, 'pages/index.html', context={'comments': cmt})
def cmt_details(req, pk):
    cmt_details = get_object_or_404(Comment, pk=pk)
    return render(req, 'pages/cmt_detail.html', context={'comments': cmt_details})
def err_404_not_found(req, exception = None):
    return render(req, 'pages/404.html', status=404)
def contact(req):
    return render(req, 'pages/contact.html')
def cart(req):
    return render(req, 'pages/cart.html')
def demo(req):
    return render(req, 'pages/demo.html')