from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from app_store.models import *

# Create your views here.
def trang_chu(request):
    danh_sach_danh_muc_cha = DanhMuc.objects.filter(danh_muc__isnull=True)
    
    return render(request, 'app_store/index-2.html', {
        'danh_sach_danh_muc_cha': danh_sach_danh_muc_cha,
    })


def gioi_thieu(request):
    danh_sach_danh_muc_cha = DanhMuc.objects.filter(danh_muc__isnull=True)
    return render(request, 'app_store/about.html', {
        'danh_sach_danh_muc_cha': danh_sach_danh_muc_cha,
    })


def lien_he(request):
    danh_sach_danh_muc_cha = DanhMuc.objects.filter(danh_muc__isnull=True)
    return render(request, 'app_store/contact.html', {
        'danh_sach_danh_muc_cha': danh_sach_danh_muc_cha,
    })


def danh_muc(request, ten_khong_dau):
    danh_sach_danh_muc_cha = DanhMuc.objects.filter(danh_muc__isnull=True)
    
    # Đọc danh sách sản phẩm từ danh mục
    danh_muc = DanhMuc.objects.get(ten_khong_dau=ten_khong_dau)
    danh_sach_san_pham = SanPham.objects.filter(danh_muc=danh_muc)

    # Phân trang
    paginator = Paginator(danh_sach_san_pham, 15)
    so_trang = request.GET.get('trang')
    try:
        danh_sach_san_pham_pager = paginator.page(so_trang)
    except PageNotAnInteger:
        # Nếu số trang không phải là int thì trả về trang 1
        danh_sach_san_pham_pager = paginator.page(1)
    except EmptyPage:
        # Nếu trang không có sản phẩm thì trả về trang cuối cùng
        danh_sach_san_pham_pager = paginator.page(paginator.num_pages)
    
    return render(request, 'app_store/shop-left-sidebar.html', {
        'danh_sach_danh_muc_cha': danh_sach_danh_muc_cha,
        'danh_sach_san_pham': danh_sach_san_pham,
        'danh_sach_san_pham_pager': danh_sach_san_pham_pager,
    })


def chi_tiet_san_pham(request):
    danh_sach_danh_muc_cha = DanhMuc.objects.filter(danh_muc__isnull=True)
    return render(request, 'app_store/single-product-slider.html', {
        'danh_sach_danh_muc_cha': danh_sach_danh_muc_cha,
    })
  
