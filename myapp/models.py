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
