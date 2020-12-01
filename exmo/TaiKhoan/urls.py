from django.urls import path

from . import views

urlpatterns = [
    path('list', views.TaiKhoanList.as_view(), name="Tai_khoan_list"),
    path('create', views.TaiKhoanCreate.as_view(), name="Tai_khoan_create"),
    path('detail/<int:pk>', views.TaiKhoanDetailUpdate.as_view(), name="Tai_khoan_detail_update"),
    path('delete/<int:pk>', views.TaiKhoanDelete.as_view(), name="Tai_khoan_delete"),
    path('grantPermission/<int:pk>', views.GrantPermission.as_view(), name="Grant_permission"),
]