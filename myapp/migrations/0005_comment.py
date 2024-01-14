# Generated by Django 5.0 on 2024-01-13 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('img_author', models.ImageField(blank=True, null=True, upload_to='post/image')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]