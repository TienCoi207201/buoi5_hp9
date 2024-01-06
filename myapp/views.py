from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Product

# Create your views here.
def demo(req):
    data = [
        {
        'name': 'Trọng Nhân',
        'age': 20
    }
    ]
    return JsonResponse(data, safe=False)
def home(req):
    products = Product.objects.all()
    return render(req, 'pages/index.html', {'products': products})
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