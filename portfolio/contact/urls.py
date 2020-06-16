from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from portfolio import settings

urlpatterns = [
    path('index/',views.contactView,name='index'),
    path('success/',views.successView, name='success'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
