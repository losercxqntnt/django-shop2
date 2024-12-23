from django.urls import path

from app_store.views import *

app_name= 'app_store'
urlpatterns = [
    path('', trang_chu, name= 'trang_chu'),
    path('gioi-thieu/', gioi_thieu, name= 'gioi_thieu'),
    path('lien-he/', lien_he, name= 'lien_he'),
    path('cua-hang/', cua_hang, name='cua_hang'),
    path('chi-tiet-san-pham/<int:id>', chi_tiet_san_pham, name= 'chi_tiet_san_pham'),
    path('search/', tim_kiem_san_pham, name='tim_kiem_san_pham'),
    path('lien-he/cam-on-cau-hoi/', cam_on_cau_hoi, name='cam_on_cau_hoi'),
]
