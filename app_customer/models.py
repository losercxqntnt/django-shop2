from django.db import models

# Create your models here.
class KhachHang(models.Model):
    ho = models.CharField(max_length=100, null=True, blank=True)
    ten = models.CharField(max_length=50, null=True, blank=True)
    ngay_sinh = models.DateField(null=True, blank=True)
    ten_dang_nhap = models.CharField(max_length=100, unique=True)
    mat_khau = models.CharField(max_length=200)
    dien_thoai = models.CharField(max_length=20, null=True, blank=True)
    dia_chi = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField()
    
    def __str__(self) -> str:
        return self.ten_dang_nhap
    