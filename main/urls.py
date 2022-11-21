from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url 
from django.views.static import serve


urlpatterns = [
    path('', views.main, name='main'),
    path('category/<slug:category_slug>/', views.main, name='product_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.detail, name='detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
