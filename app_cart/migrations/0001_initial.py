# Generated by Django 5.1.1 on 2024-11-22 16:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_customer', '0001_initial'),
        ('app_store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonHang',
            fields=[
                ('ma_don_hang', models.CharField(default='DH20241122163403', max_length=20, primary_key=True, serialize=False, unique=True)),
                ('tong_tien', models.DecimalField(decimal_places=2, max_digits=10)),
                ('trang_thai', models.BooleanField(default=False)),
                ('ngay_tao', models.DateTimeField(auto_now_add=True)),
                ('khach_hang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_customer.khachhang')),
            ],
            options={
                'ordering': ('-ngay_tao',),
            },
        ),
        migrations.CreateModel(
            name='ChiTietDonHang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('don_gia', models.DecimalField(decimal_places=2, max_digits=15)),
                ('so_luong', models.IntegerField(default=1)),
                ('giam_gia', models.DecimalField(decimal_places=2, max_digits=15)),
                ('thanh_tien', models.DecimalField(decimal_places=2, max_digits=15)),
                ('san_pham', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_store.sanpham')),
                ('don_hang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_cart.donhang')),
            ],
        ),
    ]
