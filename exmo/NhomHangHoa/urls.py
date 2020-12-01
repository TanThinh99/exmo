from django.urls import path

from . import views

urlpatterns = [
    path('list', views.NhomHangHoaList.as_view(), name="Nhom_hang_hoa_list"),
    path('create', views.NhomHangHoaCreate.as_view(), name="Nhom_hang_hoa_create"),
    path('detail/<int:pk>', views.NhomHangHoaDetail.as_view(), name="Nhom_hang_hoa_detail"),
    path('hasHangHoa/<int:pk>', views.HasHangHoa.as_view(), name="Nhom_hang_hoa_has_Hang_hoa"),
]