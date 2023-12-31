from django.db import models
# from djangoProject.models import Product
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': str(self.price)
        }

# new_product = Product.objects.create(
#     name='Nike',  # Thay 'Product Name' bằng tên sản phẩm thực
#     description='Product Description',  # Thay 'Product Description' bằng mô tả thực
#     price=10.99  # Thay 10.99 bằng giá sản phẩm thực
# )