from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from app_customer.forms import FormDangKy, FormDangNhap, FormThongTinCaNhan, FormDoiMatKhau
from app_customer.models import KhachHang
from app_customer.lib_customer import *
from app_cart.models import DonHang
# Create your views here.
def dang_nhap_dang_ky(request):
    if 's_khach_hang' in request.session:
        return redirect('app_store:trang_chu')
    thong_bao = ''
    
   # Đăng ký
    form_dang_ky = FormDangKy()
    if request.POST.get('btnDangKy'):
        form_dang_ky = FormDangKy(request.POST)
        if form_dang_ky.is_valid():
            hasher = PBKDF2PasswordHasher()
            post = form_dang_ky.save(commit=False)
            post.mat_khau = hasher.encode(form_dang_ky.cleaned_data['mat_khau'], salt=salt)
            post.save()
            thong_bao = '''
                <div class="alert alert-success" role="alert">
                    Đăng ký thành viên thành công!
                </div>'''
        else:
            thong_bao = '''
                <div class="alert alert-danger" role="alert">
                    Đăng ký thành viên thất bại!
                </div>'''
            
     # Đăng nhập
    form_dang_nhap = FormDangNhap()
    if request.POST.get('btnDangNhap'):
        form_dang_nhap = FormDangNhap(request.POST)
        if form_dang_nhap.is_valid():
            hasher = PBKDF2PasswordHasher()
            ten_dang_nhap = form_dang_nhap.cleaned_data['ten_dang_nhap']
            mat_khau = hasher.encode(form_dang_nhap.cleaned_data['mat_khau'], salt=salt)
            khach_hang = KhachHang.objects.filter(ten_dang_nhap=ten_dang_nhap, mat_khau=mat_khau)
            if khach_hang:
                # dict_khach_hang = khach_hang.values().first()
                request.session['s_khach_hang'] = khach_hang.first().id
                return redirect('app_store:trang_chu')
            else:
                thong_bao = '''
                <div class="alert alert-danger" role="alert">
                    Đăng nhập thất bại!
                </div>'''
        else:
            thong_bao = '''
            <div class="alert alert-danger" role="alert">
                Thông tin nhập không hợp lệ!
            </div>'''
    
    return render(request, 'app_customer/login.html', {
        'form_dang_ky': form_dang_ky,
        'form_dang_nhap': form_dang_nhap,
        'thong_bao': thong_bao,
    })


def tai_khoan_cua_toi(request):
    if 's_khach_hang' not in request.session:
        return redirect('app_customer:dang_nhap')
    
    # Thông tin cá nhân
    thong_bao_cap_nhat_thong_tin = ''
    khach_hang = KhachHang.objects.get(id=request.session['s_khach_hang'])
    form_thong_tin = FormThongTinCaNhan(instance=khach_hang)
    if request.POST.get('btnCapNhat'):
        form_thong_tin = FormThongTinCaNhan(request.POST, instance=khach_hang)
        if form_thong_tin.is_valid():
            form_thong_tin.save()
            thong_bao_cap_nhat_thong_tin = '''
                <div class="alert alert-success" role="alert">
                    Cập nhật thông tin thành công!
                </div>'''
        else:
            thong_bao_cap_nhat_thong_tin = '''
                <div class="alert alert-danger" role="alert">
                    Thông tin không hợp lệ!
                </div>'''
        
    
    # Đổi mật khẩu
    thong_bao_doi_mat_khau = ''
    form_doi_mat_khau = FormDoiMatKhau()
    if request.POST.get('btnDoiMatKhau'):
        form_doi_mat_khau = FormDoiMatKhau(request.POST)
        if form_doi_mat_khau.is_valid():
            hasher = PBKDF2PasswordHasher()
            mat_khau_cu = hasher.encode(form_doi_mat_khau.cleaned_data['mat_khau_cu'], salt=salt)
            mat_khau_moi = hasher.encode(form_doi_mat_khau.cleaned_data['mat_khau_moi'], salt=salt)
            xac_nhan_mat_khau_moi = hasher.encode(form_doi_mat_khau.cleaned_data['xac_nhan_mat_khau_moi'], salt=salt)
            if mat_khau_cu == khach_hang.mat_khau:
                if mat_khau_moi == xac_nhan_mat_khau_moi:
                    khach_hang.mat_khau = mat_khau_moi
                    khach_hang.save()
                    thong_bao_doi_mat_khau = '''
                        <div class="alert alert-success" role="alert">
                            Đổi mật khẩu thành công!
                        </div>'''
                else:
                    thong_bao_doi_mat_khau = '''
                    <div class="alert alert-danger" role="alert">
                        Mật khẩu mới và Xác nhận mật khẩu không khớp!
                    </div>'''
            else:
                thong_bao_doi_mat_khau = '''
                    <div class="alert alert-danger" role="alert">
                        Mật khẩu cũ không đúng!
                    </div>'''
        else:
            thong_bao_doi_mat_khau = '''
                <div class="alert alert-danger" role="alert">
                    Thông tin không hợp lệ!
                </div>'''
    
    # Danh sách đơn hàng theo tài khoản
    danh_sach_don_hang = DonHang.objects.filter(khach_hang=khach_hang)
    
    return render(request, 'app_customer/my-account.html', {
        'form_thong_tin': form_thong_tin,
        'form_doi_mat_khau': form_doi_mat_khau,
        'thong_bao_doi_mat_khau': thong_bao_doi_mat_khau,
        'thong_bao_cap_nhat_thong_tin': thong_bao_cap_nhat_thong_tin,
        'danh_sach_don_hang': danh_sach_don_hang,
    })

def dang_xuat(request):
    if 's_khach_hang' in request.session:
        del request.session['s_khach_hang']
    return redirect('app_customer:dang_nhap')