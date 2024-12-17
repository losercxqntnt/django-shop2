from django.urls import path
from app_news.views import *

app_name= 'app_news'
urlpatterns = [
    path('tin-tuc/',tin_tuc,name='tin_tuc'),
    path('chi-tiet-tin-tuc/',chi_tiet_tin_tuc,name='chi_tiet_tin_tuc'),

  
]
