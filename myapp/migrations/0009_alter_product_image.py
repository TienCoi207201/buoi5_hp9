# Generated by Django 5.0 on 2024-03-03 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_product_origin_product_trademark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product'),
        ),
    ]
