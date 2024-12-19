from django.contrib import admin
from .models import KhachHang

@admin.register(KhachHang)
class KhachHangAdmin(admin.ModelAdmin):
    list_display = ('ten_dang_nhap', 'ho', 'ten', 'email', 'dien_thoai')  # Các trường sẽ hiển thị trong danh sách
    search_fields = ('ten_dang_nhap', 'email', 'ho', 'ten')  # Cho phép tìm kiếm theo các trường này
    list_filter = ('ngay_sinh',)  # Bộ lọc bên cạnh danh sách
    ordering = ('ten_dang_nhap',)  # Sắp xếp theo tên đăng nhập
    fieldsets = (  # Cấu trúc bố cục chi tiết trang chỉnh sửa
        (None, {
            'fields': ('ten_dang_nhap', 'mat_khau')
        }),
        ('Thông tin cá nhân', {
            'fields': ('ho', 'ten', 'ngay_sinh', 'dien_thoai', 'dia_chi', 'email')
        }),
    )
