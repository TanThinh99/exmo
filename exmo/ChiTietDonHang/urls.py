from django.urls import path

from . import views

urlpatterns = [
    path('create', views.ChiTietDonHangCreate.as_view(), name='Chi_tiet_don_hang_create'),
]