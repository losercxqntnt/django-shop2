from django.urls import path
from app_customer.views import *

app_name= 'app_customer'
urlpatterns = [
 path('dang-nhap/',dang_nhap_dang_ky,name='dang_nhap'),
 path('tai-khoan-cua-toi/',tai_khoan_cua_toi,name='tai_khoan_cua_toi'),
 path('dang-xuat/',dang_xuat,name='dang_xuat'),
 
    
]
