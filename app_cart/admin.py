from django.contrib import admin
from .models import DonHang, ChiTietDonHang, KhuyenMai


class ChiTietDonHangInline(admin.TabularInline):  # Sử dụng inline để hiển thị chi tiết đơn hàng trong đơn hàng
    model = ChiTietDonHang
    extra = 1  # Số dòng trống cho phép thêm mới
    fields = ('san_pham', 'don_gia', 'so_luong', 'giam_gia', 'thanh_tien')  # Các trường hiển thị trong inline
    readonly_fields = ('thanh_tien',)  # Chỉ hiển thị (không chỉnh sửa) `thanh_tien`

@admin.register(DonHang)
class DonHangAdmin(admin.ModelAdmin):
    list_display = ('ma_don_hang', 'khach_hang', 'tong_tien', 'trang_thai', 'ngay_tao')  # Hiển thị danh sách
    search_fields = ('ma_don_hang', 'khach_hang__ten_dang_nhap')  # Cho phép tìm kiếm theo mã đơn hàng và tên khách hàng
    list_filter = ('trang_thai', 'ngay_tao')  # Bộ lọc theo trạng thái và ngày tạo
    ordering = ('-ngay_tao',)  # Sắp xếp theo ngày tạo mới nhất
    inlines = [ChiTietDonHangInline]  # Thêm inline chi tiết đơn hàng
    fieldsets = (
        (None, {
            'fields': ('ma_don_hang', 'khach_hang', 'tong_tien', 'trang_thai')
        }),
        ('Thông tin khác', {
            'fields': ('ghi_chu',),
            'classes': ('collapse',),  # Thu gọn phần ghi chú
        }),
    )
    readonly_fields = ('tong_tien', 'ngay_tao')  # Các trường chỉ hiển thị (không chỉnh sửa)

@admin.register(ChiTietDonHang)
class ChiTietDonHangAdmin(admin.ModelAdmin):
    list_display = ('don_hang', 'san_pham', 'don_gia', 'so_luong', 'giam_gia', 'thanh_tien')  # Hiển thị danh sách
    search_fields = ('don_hang__ma_don_hang', 'san_pham__ten')  # Cho phép tìm kiếm theo mã đơn hàng và tên sản phẩm
    list_filter = ('don_hang__ngay_tao',)  # Bộ lọc theo ngày tạo đơn hàng

@admin.register(KhuyenMai)
class KhuyenMaiAdmin(admin.ModelAdmin):
    list_display = ('ma_khuyen_mai', 'san_pham', 'ti_le_khuyen_mai', 'ngay_tao')
    search_fields = ('ma_khuyen_mai', 'san_pham__ten')
    list_filter = ('ngay_tao',)
    ordering = ('-ngay_tao',)
