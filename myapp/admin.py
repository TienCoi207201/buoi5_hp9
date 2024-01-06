from django.contrib import admin
from .models import Product, Post
# Register your models here.
# class AdminProduct(admin.ModelAdmin):
#     list_products = ('name', 'description', 'price')

admin.site.register(Product)
admin.site.register(Post)