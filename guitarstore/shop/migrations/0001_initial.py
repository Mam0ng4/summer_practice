# Generated by Django 5.0.6 on 2024-06-06 15:49

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GuitarCategory',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SimpleOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_status', models.CharField(default='pending', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Guitar',
            fields=[
                ('guitar_id', models.AutoField(primary_key=True, serialize=False)),
                ('guitar_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('in_stock', models.BooleanField(default=True)),
                ('manufacturer', models.CharField(max_length=100)),
                ('country_of_origin', models.CharField(max_length=100)),
                ('year_of_production', models.IntegerField()),
                ('image_url', models.URLField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.guitarcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_status', models.CharField(default='pending', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderGuitar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('guitar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.guitar')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.order')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('guitars_count', models.PositiveIntegerField()),
                ('guitar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.guitar')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SimpleOrderGuitar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('guitar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.guitar')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.simpleorder')),
            ],
        ),
    ]
