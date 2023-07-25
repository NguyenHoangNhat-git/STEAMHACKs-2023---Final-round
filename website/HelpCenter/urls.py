from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from .views.home import home

urlpatterns = [
    path('', home, name='Home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
