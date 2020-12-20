from django.urls import path

from . import views

urlpatterns = [
    path('list', views.DonHangList.as_view(), name="Don_hang_list"),
    path('create', views.DonHangCreate.as_view(), name="Don_hang_create"),
    path('detail/<int:pk>', views.DonHangDetail.as_view(), name="Don_hang_detail"),
    path('delete/<int:pk>', views.DonHangDelete.as_view(), name="Don_hang_delete"),
    path('hasChiTietDonHang/<int:pk>', views.HasChiTietDonHang.as_view(), name='Don_hang_has_Chi_tiet_don_hang'),
    path('pass/<int:pk>', views.PassDonHang.as_view(), name="Duyet_don_hang"),
]