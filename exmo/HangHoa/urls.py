from django.urls import path

from . import views

urlpatterns = [
    path('list', views.HangHoaList.as_view(), name='Hang_hoa_list'),
    path('create', views.HangHoaCreate.as_view(), name='Hang_hoa_create'),
    path('detail/<int:pk>', views.HangHoaDetail.as_view(), name='Hang_hoa_detail'),
    path('update/<int:pk>', views.HangHoaUpdate.as_view(), name='Hang_hoa_update'),
    path('delete/<int:pk>', views.HangHoaDelete.as_view(), name='Hang_hoa_delete'),
]