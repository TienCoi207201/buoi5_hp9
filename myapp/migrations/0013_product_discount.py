# Generated by Django 4.2.17 on 2024-12-16 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
    ]
