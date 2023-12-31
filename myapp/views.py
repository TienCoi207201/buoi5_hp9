from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Product

# Create your views here.
def demo(req):
    products = Product.objects.all()
    products_data = [product.to_dict() for product in products]
    return JsonResponse(req, {'products': products_data}, safe=False)
# def home(req):
