from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url 
from django.views.static import serve
from .views import *

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post<int:id>/', post_detail, name='post_detail'),
    # path('subscribe', subscribe, name='subscribe')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
