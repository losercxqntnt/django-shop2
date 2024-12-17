from django import forms
from app_customer.models import KhachHang


class FormDangKy(forms.ModelForm):
    class Meta:
        model = KhachHang
        fields = '__all__'
        widgets = {
            'ten_dang_nhap': forms.TextInput(attrs={'placeholder': 'Tên đăng nhập'}),
            'mat_khau': forms.PasswordInput(attrs={'placeholder': 'Mật khẩu'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
        }

class FormDangNhap(forms.Form):
    ten_dang_nhap= forms.CharField(max_length=100,
                                   widget=forms.TextInput(attrs={'placehoder':'tên đăng nhập',}))
    mat_khau=forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'placehoder':'mật_khẩu',
    }))
class FormThongTinCaNhan(forms.ModelForm):
    class Meta:
        model = KhachHang
        fields = ['ten_dang_nhap', 'ho', 'ten', 'ngay_sinh', 'email', 'dien_thoai', 'dia_chi']
        labels = {
            'ten_dang_nhap': 'Tên đăng nhập',
            'ho': 'Họ',
            'ten': 'Tên',
            'ngay_sinh': 'Ngày sinh',
            'email': 'Email',
            'dien_thoai': 'Điện thoại',
            'dia_chi': 'Địa chỉ',
        }
        widgets = {
            'ten_dang_nhap': forms.TextInput(attrs={'placeholder': 'Tên đăng nhập', 'readonly': True, 'style': 'background-color: #f0f0f0'}),
            'ho': forms.TextInput(attrs={'placeholder': 'Họ'}),
            'ten': forms.TextInput(attrs={'placeholder': 'Tên'}),
            'ngay_sinh': forms.DateInput(attrs={'type': 'date'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'dien_thoai': forms.TextInput(attrs={'placeholder': 'Điện thoại'}),
            'dia_chi': forms.Textarea(attrs={'placeholder': 'Địa chỉ', 'class': 'form-control', 'rows': 3}),
        }


class FormDoiMatKhau(forms.ModelForm):
    mat_khau_cu = forms.CharField(max_length=200, label='Mật khẩu cũ', widget=forms.PasswordInput(attrs={'placeholder': 'Mật khẩu cũ'}))
    mat_khau_moi = forms.CharField(max_length=200, label='Mật khẩu mới', widget=forms.PasswordInput(attrs={'placeholder': 'Mật khẩu mới'}))
    xac_nhan_mat_khau_moi = forms.CharField(max_length=200, label='Xác nhận mật khẩu mới', widget=forms.PasswordInput(attrs={'placeholder': 'Xác nhận mật khẩu mới'}))

    class Meta:
        model = KhachHang
        fields = ['mat_khau_cu', 'mat_khau_moi', 'xac_nhan_mat_khau_moi']