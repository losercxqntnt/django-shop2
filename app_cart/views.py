from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from app_cart.cart import GioHang
from app_cart.models import DonHang, ChiTietDonHang, KhuyenMai
from app_store.models import SanPham
from app_customer.models import KhachHang
from datetime import datetime
from decimal import Decimal

# Create your views here.
def gio_hang(request):
    if request.method == 'GET':
        action = request.GET.get('action')
        if action == 'btnTimKiem':
            return tim_kiem_san_pham(request)

    gio_hang = GioHang(request)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'btnCapNhatGioHang':
            gio_hang_moi = {}
            for gh in gio_hang:
                so_luong_moi = int(request.POST.get(f'so_luong_{gh["san_pham"].id}'))
                if so_luong_moi != 0:
                    dict_gio_hang = {
                        str(gh['san_pham'].id): {
                            'so_luong': so_luong_moi,
                            'gia_ban': str(gh['gia_ban']),
                            'giam_gia': str(gh['giam_gia']),
                        }
                    }
                    gio_hang_moi.update(dict_gio_hang)
                    gh['so_luong'] = so_luong_moi
                else:
                    # Nếu số lượng = 0 thì xóa SP khỏi giỏ hàng
                    san_pham = get_object_or_404(SanPham, id=gh['san_pham'].id)
                    gio_hang.xoa_san_pham(san_pham)

            request.session[settings.CART_SESSION_ID] = gio_hang_moi

        if action == 'btnApDungKhuyenMai':
            gio_hang_moi = {}
            ma_khuyen_mai = request.POST.get('ma_khuyen_mai')
            khuyen_mai = KhuyenMai.objects.filter(ma_khuyen_mai=ma_khuyen_mai).first()
            if khuyen_mai is not None and len(gio_hang) >= 1:
                for gh in gio_hang:
                    san_pham_id = gh['san_pham'].id
                    if san_pham_id == khuyen_mai.san_pham.id:
                        gh['giam_gia'] = khuyen_mai.ti_le_khuyen_mai / 100

                    dict_gio_hang = {
                        str(gh['san_pham'].id): {
                            'so_luong': gh['so_luong'],
                            'gia_ban': str(gh['gia_ban']),
                            'giam_gia': str(gh['giam_gia']),
                        }
                    }
                    gio_hang_moi.update(dict_gio_hang)

                request.session[settings.CART_SESSION_ID] = gio_hang_moi

    return render(request, 'app_cart/cart.html', {
        'gio_hang': gio_hang
    })

def thanh_toan(request):
    if request.method == 'GET':
        action = request.GET.get('action')
        if action == 'btnTimKiem':
            return tim_kiem_san_pham(request)

    if 's_khach_hang' not in request.session:
        return redirect('app_cart:gio_hang')
    
    gio_hang = GioHang(request)
    khach_hang = KhachHang.objects.get(id=request.session['s_khach_hang'])
    
    if request.POST.get('btnDatHang'):
        if len(gio_hang) < 1:
            redirect('app_cart:gio_hang')
        
        # Ghi thông tin đơn hàng
        ma_don_hang = datetime.now().strftime('DH%Y%m%d%H%M%S')
        ghi_chu = request.POST.get('ghi_chu')
        don_hang = DonHang.objects.create(ma_don_hang=ma_don_hang,
                                          khach_hang=khach_hang,
                                          tong_tien=gio_hang.tong_tien_phai_tra(),
                                          ghi_chu=ghi_chu)
        
        # Ghi thông tin chi tiết đơn hàng
        if don_hang:
            for gh in gio_hang:
                ChiTietDonHang.objects.create(don_hang=don_hang,
                                              san_pham=gh['san_pham'],
                                              don_gia=gh['gia_ban'],
                                              so_luong=gh['so_luong'],
                                              giam_gia=gh['giam_gia'],
                                              thanh_tien=gh['thanh_tien'])
            else:
                # Gửi mail

                # Xóa tất cả các SP trong giỏ hàng
                gio_hang.xoa_gio_hang()
                return render(request, 'app_cart/thank-you-page.html')

    san_phams = []
    tong_thanh_tien = 0
    if len(gio_hang) >= 1:
        for gh in gio_hang:
            san_pham = {
                "ten_san_pham": gh['san_pham'],
                "don_gia": gh['gia_ban'],
                "so_luong": gh['so_luong'],
            }
            tong_thanh_tien += gh['thanh_tien']
            san_phams.append(san_pham)

    return render(request, 'app_cart/checkout.html', {
        'san_phams': san_phams,
        'tong_thanh_tien': tong_thanh_tien
    })

def gio_hang_rong(request):
    return render(request, 'app_cart/empty-cart.html')

def cam_on(request):
    return render(request, 'app_cart/thank-you-page.html')

def mua_ngay(request, san_pham_id):
    gio_hang = GioHang(request)
    san_pham = get_object_or_404(SanPham, id=san_pham_id)
    if request.POST.get('so_luong'):
        so_luong = int(request.POST.get('so_luong'))
        gio_hang.them_vao_gio_hang(san_pham, so_luong)
    return redirect('app_cart:gio_hang')

def xoa_san_pham(request, san_pham_id):
    gio_hang = GioHang(request)
    san_pham = get_object_or_404(SanPham, id=san_pham_id)
    gio_hang.xoa_san_pham(san_pham)
    return redirect('app_cart:gio_hang')

def xoa_gio_hang(request):
    gio_hang = GioHang(request)
    gio_hang.xoa_gio_hang()
    return redirect('app_cart:gio_hang')

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
