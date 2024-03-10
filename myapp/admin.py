from django.contrib import admin
from .models import Product, Post, Comment
# Register your models here.
# class AdminProduct(admin.ModelAdmin):
#     list_products = ('name', 'description', 'price')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'origin', 'trademark')
    # search_fields = ('name', 'description')


admin.site.register(Product, ProductAdmin)
admin.site.register(Post)
admin.site.register(Comment)