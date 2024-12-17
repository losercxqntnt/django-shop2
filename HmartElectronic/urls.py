from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_store.urls')),
    path('', include('app_customer.urls')),
    path('', include('app_cart.urls')),
    path('', include('app_report.urls')),
    path('', include('app_news.urls')),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
]


urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

