from django.contrib.auth.models import User
from django.db import models
# from djangoProject.models import Product
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_image/', null=True, blank=True)
    description = models.TextField(max_length=1000, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    def getName(self):
        return self.name
    def getImage(self):
        return self.image
    def getDescription(self):
        return self.description
    def getPrice(self):
        return self.price

class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(upload_to='post_image', null=True, blank=True)
    def getTitle(self):
        return self.title
    def getDate(self):
        return self.date
    def getContent(self):
        return self.content
    def getDescription(self):
        return self.description

class Comment(models.Model):
    content = models.TextField()
    author = User
    img_author = models.ImageField(upload_to='post/image', null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)