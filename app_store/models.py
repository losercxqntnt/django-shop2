from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.
class DanhMuc(models.Model):
    danh_muc = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    ten_danh_muc = models.CharField(max_length=255)
    ten_khong_dau = models.CharField(max_length=255, null=True, blank=True)
    mo_ta = models.TextField(null=True, blank=True)
    hinh_anh = models.ImageField(upload_to='images/danh-muc', default='images/danh-muc/no-image.jpg')

    def __str__(self):
        return self.ten_danh_muc


class ThuongHieu(models.Model):
    ten_thuong_hieu = models.CharField(max_length=255)
    mo_ta = models.TextField(null=True, blank=True)
    hinh_anh = models.ImageField(upload_to='images/thuong-hieu', default='images/thuong-hieu/no-image.jpg')

    def __str__(self):
        return self.ten_thuong_hieu


class SanPham(models.Model):
    danh_muc = models.ForeignKey(DanhMuc, on_delete=models.CASCADE)
    thuong_hieu = models.ForeignKey(ThuongHieu, on_delete=models.CASCADE)
    ten_san_pham = models.CharField(max_length=255)
    ten_khong_dau = models.CharField(max_length=255, null=True, blank=True)
    mo_ta = models.TextField(null=True, blank=True)
    sku = models.CharField(max_length=255)
    gia_ban = models.BigIntegerField(default=0)
    gia_goc = models.BigIntegerField(default=0)
    thong_so_ky_thuat = models.TextField(null=True, blank=True)
    ngay_tao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ten_san_pham


class HinhSanPham(models.Model):
    san_pham = models.ForeignKey(SanPham, on_delete=models.CASCADE)
    hinh_anh = models.ImageField(upload_to='images/san-pham', default='images/san-pham/no-image.jpg', max_length=200)
    dai_dien = models.BooleanField(default=False)

    def __str__(self):
        return self.hinh_anh.url

    class Meta:
        ordering = ['-dai_dien']


class GioiThieu(models.Model):
    id = models.IntegerField(primary_key=True)
    tieu_de = models.CharField(max_length=255)
    noi_dung = CKEditor5Field(config_name='extends')

    def __str__(self):
        return self.tieu_de


class LienHe(models.Model):
    ho_ten = models.CharField(max_length=150)
    email = models.EmailField()
    tieu_de = models.CharField(max_length=200)
    noi_dung = models.TextField()
    ngay_tao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ho_ten


class Slider(models.Model):
    ten = models.CharField(max_length=255)
    hinh_anh = models.ImageField(upload_to='images/slider', default='images/slider/no-image.jpg')
    noi_dung = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    thu_tu = models.IntegerField(default=0)

    def __str__(self):
        return self.ten

    class Meta:
        ordering = ['thu_tu']