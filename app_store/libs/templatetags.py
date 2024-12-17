from django import template
from app_store.models import DanhMuc
from app_customer.models import KhachHang



register = template.Library()


@register.filter(name='lay_danh_sach_danh_muc_con_tu_danh_muc_cha')
def lay_danh_sach_danh_muc_con_tu_danh_muc_cha(danh_muc_cha):
    return DanhMuc.objects.filter(danh_muc=danh_muc_cha)

@register.filter(name='lay_thong_tin_khach_hang_tu_id')
def lay_thong_tin_khach_hang_tu_id(khach_hang_id):
    return KhachHang.objects.get(id=khach_hang_id)