from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt

from app_store.models import *

# Create your views here.
def trang_chu(request):
    if request.method == 'GET':
        action = request.GET.get('action')
        if action == 'btnTimKiem':
            return tim_kiem_san_pham(request)

    # Đọc danh sách sản phẩm quần áo từ danh mục
    default_ten_danh_muc = 'quan-ao'
    danh_muc = DanhMuc.objects.get(ten_khong_dau=default_ten_danh_muc)
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

    return render(request, 'app_store/index-2.html', {
        'danh_sach_san_pham': danh_sach_san_pham,
        'danh_sach_san_pham_pager': danh_sach_san_pham_pager,
    })


def gioi_thieu(request):
    if request.method == 'GET':
        action = request.GET.get('action')
        if action == 'btnTimKiem':
            return tim_kiem_san_pham(request)

    danh_sach_danh_muc_cha = DanhMuc.objects.filter(danh_muc__isnull=True)
    return render(request, 'app_store/about.html', {
        'danh_sach_danh_muc_cha': danh_sach_danh_muc_cha,
    })


def lien_he(request):
    if request.method == 'GET':
        action = request.GET.get('action')
        if action == 'btnTimKiem':
            return tim_kiem_san_pham(request)

    if request.method == 'POST':
        ho_ten = request.POST.get('name')
        email = request.POST.get('email')
        tieu_de = request.POST.get('subject')
        noi_dung = request.POST.get('message')
        lien_he_moi = LienHe.objects.create(ho_ten=ho_ten,
                                          email=email,
                                          tieu_de=tieu_de,
                                          noi_dung=noi_dung)

        return cam_on_cau_hoi(request)

    danh_sach_danh_muc_cha = DanhMuc.objects.filter(danh_muc__isnull=True)
    return render(request, 'app_store/contact.html', {
        'danh_sach_danh_muc_cha': danh_sach_danh_muc_cha,
    })


def cua_hang(request):
    if request.method == 'GET':
        action = request.GET.get('action')
        if action == 'btnTimKiem':
            return tim_kiem_san_pham(request)

    # Đọc danh sách sản phẩm quần áo từ danh mục
    default_ten_danh_muc = 'quan-ao'
    danh_muc = DanhMuc.objects.get(ten_khong_dau=default_ten_danh_muc)
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
        'danh_sach_san_pham': danh_sach_san_pham,
        'danh_sach_san_pham_pager': danh_sach_san_pham_pager,
    })


def chi_tiet_san_pham(request, id):
    if request.method == 'GET':
        action = request.GET.get('action')
        if action == 'btnTimKiem':
            return tim_kiem_san_pham(request)

    san_pham = get_object_or_404(SanPham, id=id)
    return render(request, 'app_store/single-product-slider.html', {
        'san_pham': san_pham,
    })

def tim_kiem_san_pham(request):
    search_text = request.GET.get('text_search')
    san_pham_filters = []
    danh_sach_san_pham = SanPham.objects.all()
    if search_text is not None:
        san_pham_filters = danh_sach_san_pham.filter(ten_san_pham__icontains=search_text)
    return render(request, 'app_store/shop-left-sidebar.html', {
        'danh_sach_san_pham': san_pham_filters,
        'danh_sach_san_pham_pager': san_pham_filters,
    })

def cam_on_cau_hoi(request):
    return render(request, 'app_store/thank-you-page.html')