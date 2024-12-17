from django.db import models
from app_customer.models import KhachHang
from app_store.models import SanPham



# Create your models here.
class DonHang(models.Model):
    ma_don_hang = models.CharField(primary_key=True, max_length=20, unique=True)
    khach_hang = models.ForeignKey(KhachHang, on_delete=models.CASCADE)
    tong_tien = models.DecimalField(max_digits=10, decimal_places=2)
    trang_thai = models.BooleanField(default=False)
    ngay_tao = models.DateTimeField(auto_now_add=True)
    ghi_chu = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ('-ngay_tao',)

    def __str__(self):
        return f'{self.ma_don_hang}'


class ChiTietDonHang(models.Model):
    don_hang = models.ForeignKey(DonHang, on_delete=models.CASCADE)
    san_pham = models.ForeignKey(SanPham, on_delete=models.CASCADE)
    don_gia = models.DecimalField(max_digits=15, decimal_places=2)
    so_luong = models.IntegerField(default=1)
    giam_gia = models.DecimalField(max_digits=15, decimal_places=2)
    thanh_tien = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return str(self.don_hang)

