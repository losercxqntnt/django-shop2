from django.urls import path
from app_store.views import *

app_name= 'app_store'
urlpatterns = [
    path('', trang_chu, name= 'trang_chu'),
    path('gioi-thieu/', gioi_thieu, name= 'gioi_thieu'),
    path('lien-he/', lien_he, name= 'lien_he'),
    path('danh-muc/<slug:ten_khong_dau>/', danh_muc, name='danh_muc'),
    path('chi-tiet-san-pham/', chi_tiet_san_pham, name= 'chi_tiet_san_pham'),
    
]
