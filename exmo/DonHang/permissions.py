from rest_framework.permissions import BasePermission

from TaiKhoan.models import Taikhoan


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        username = str(request.user)
        user = Taikhoan.objects.get(username=username)
        return user.isadmin


class IsAdminOrOwnerUser(BasePermission):

    def has_object_permission(self, request, view, obj):
        username = str(request.user)
        user = Taikhoan.objects.get(username=username)

        print(str(obj.makh)+', '+str(user.matk)+', '+str(user.isadmin))
        return (obj.makh == user) or user.isadmin