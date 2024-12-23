from django.urls import path
from app_cart.views import *

app_name= 'app_cart'
urlpatterns = [
    path('gio-hang/', gio_hang,name='gio_hang'),
    path('thanh-toan/', thanh_toan,name='thanh_toan'),
    path('gio-hang-rong/',gio_hang_rong,name='gio_hang_rong'),
    path('cam-on/', cam_on,name='cam_on'),
    path('mua-ngay/<int:san_pham_id>/', mua_ngay, name='mua_ngay'),
    path('xoa-gio-hang/', xoa_gio_hang, name='xoa_gio_hang'),
    path('xoa-san-pham/<int:san_pham_id>/', xoa_san_pham, name='xoa_san_pham'),
]
