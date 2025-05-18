from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Product, Post, Comment
from django.core.serializers import  serialize
from django.views.generic import ListView, DetailView
from .form import RegisterForm, ProductForm
from django.contrib.auth.decorators import login_required

# Create your views here.
#Syntax class view
# class tên_class(View):
#    model = tên_model
#    template_name = 'tên_template'
#    context_object_name = 'tên_context'
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
def showData(req):
    products = Product.objects.all()
    return render(req, 'pages/demo.html', context= { 'data': products })

class HomeListView(ListView):
    # posts = Post.objects.all()
    # comment = Comment.objects.all()
    # image_path = 'static/images/couch.png'
    # return render(req, 'pages/index.html', {'posts': posts, 'image_path': image_path, 'comments': comment})
    model = Product
    template_name = "pages/index.html"
    context_object_name = 'products'
class ProductListView(ListView):
    # products = Product.objects.all()
    # filter = Product.objects.filter()
    # return render(req, 'pages/product.html', context={'products': products})
    model =Product
    template_name = "pages/product.html"
    context_object_name = 'products'

#return JsonResponse(data,json_dumps_params={'ensure_ascii': False}, safe=False)

    
class CommentListView(ListView):
    model = Comment
    # cmt_json = serialize('json', cmt)
    template_name = "pages/index.html"
    # return JsonResponse(cmt_json, json_dumps_params={'ensure_ascii': False}, safe=False)
    context_object_name = 'comments'
def cmt_details(req, pk):
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
        username = req.POST.get('username')
        password = req.POST.get('password')
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

# def signup_user(req):
#     if req.method == "POST":
#         form = RegisterForm(req.POST or None) 
#         if form.is_valid():
#             user = form.save()
#             login(req, user) 
#             print("User save:", user.username)
#             return redirect("home:home")  
#     else:
#         form = RegisterForm()
#     return render(req, "pages/signup.html", { "form": form })
def signup_user(request):
    print("Request method:", request.method)
    if request.method == 'POST':
        print("Form data:", request.POST)
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Đăng ký thành công!')
            return redirect('home:home')
        else:
            print("Form errors:", form.errors)
            messages.error(request, 'Có lỗi trong form, vui lòng kiểm tra lại.')
    else:
        form = RegisterForm()
    return render(request, 'pages/signup.html', {'form': form})

def logout_user(req):
    logout(req)
    return redirect("home:home")

def viewProduct(req):
    products = Product.objects.all()
    return render(req, "pages/product/view_product.html", context = { 'products': products })

def editProduct(req, pk):
    product = get_object_or_404(Product, id = pk)
    form = ProductForm(req.POST, req.FILES, instance = product or None)
    if req.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("view_product")
        else:
            form = ProductForm(instance=product)

    return render(req, "pages/product/edit_product.html", context= { 'form': form, 'product': product })

def deleteProduct(req, pk):
    product = get_object_or_404(Product, id = pk)
    product.delete()
    return redirect("view_product")

def addProduct(req):
    form = ProductForm(req.POST, req.FILES)
    if req.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("view_product")
        else:
            form = ProductForm()
    return render(req, "pages/product/add_product.html", context = { 'form': form })

def produduct_req(req):
    product = Product.objects.all()
    #convert to json
    product_convert = serialize('json', product)
    return JsonResponse(product_convert, safe=False, json_dumps_params={'ensure_ascii': False})

def filterProduct(req):
    product = Product.objects.filter(price__gt = 10000)
    product_convert = serialize('json', product)
    return JsonResponse(product_convert, safe=False, json_dumps_params={'ensure_ascii': False})