from django.contrib import admin
from .models import DanhMuc, ThuongHieu, SanPham, HinhSanPham, GioiThieu, LienHe, Slider


@admin.register(DanhMuc)
class DanhMucAdmin(admin.ModelAdmin):
    list_display = ('id', 'ten_danh_muc', 'ten_khong_dau', 'danh_muc', 'mo_ta', 'hinh_anh')
    list_filter = ('danh_muc',)
    search_fields = ('ten_danh_muc', 'ten_khong_dau', 'mo_ta')
    prepopulated_fields = {'ten_khong_dau': ('ten_danh_muc',)}
    ordering = ('ten_danh_muc',)


@admin.register(ThuongHieu)
class ThuongHieuAdmin(admin.ModelAdmin):
    list_display = ('id', 'ten_thuong_hieu', 'mo_ta', 'hinh_anh')
    search_fields = ('ten_thuong_hieu', 'mo_ta')
    ordering = ('ten_thuong_hieu',)


@admin.register(SanPham)
class SanPhamAdmin(admin.ModelAdmin):
    list_display = ('id', 'ten_san_pham', 'ten_khong_dau', 'danh_muc', 'thuong_hieu', 'gia_ban', 'gia_goc', 'ngay_tao')
    list_filter = ('danh_muc', 'thuong_hieu', 'ngay_tao')
    search_fields = ('ten_san_pham', 'ten_khong_dau', 'mo_ta', 'sku')
    prepopulated_fields = {'ten_khong_dau': ('ten_san_pham',)}
    ordering = ('-ngay_tao',)


@admin.register(HinhSanPham)
class HinhSanPhamAdmin(admin.ModelAdmin):
    list_display = ('id', 'san_pham', 'hinh_anh', 'dai_dien')
    list_filter = ('dai_dien', 'san_pham')
    search_fields = ('san_pham__ten_san_pham',)
    ordering = ['-dai_dien']


@admin.register(GioiThieu)
class GioiThieuAdmin(admin.ModelAdmin):
    list_display = ('id', 'tieu_de')
    search_fields = ('tieu_de', 'noi_dung')


@admin.register(LienHe)
class LienHeAdmin(admin.ModelAdmin):
    list_display = ('id', 'ho_ten', 'email', 'tieu_de', 'ngay_tao')
    search_fields = ('ho_ten', 'email', 'tieu_de', 'noi_dung')
    ordering = ('-ngay_tao',)


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'ten', 'thu_tu', 'hinh_anh', 'url', 'noi_dung')
    search_fields = ('ten', 'noi_dung', 'url')
    ordering = ('thu_tu',)
