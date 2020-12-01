from rest_framework.permissions import BasePermission

from .models import Taikhoan

class IsAdmin(BasePermission):
    
    def has_permission(self, request, view):
        username = str(request.user)
        user = Taikhoan.objects.get(username=username)
        return user.isadmin

    def has_object_permission(self, request, view, obj):
        username = str(request.user)
        user = Taikhoan.objects.get(username=username)
        return user.isadmin


class IsOwnerUser(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        username = str(request.user)
        user = Taikhoan.objects.get(username=username)
        print(username)
        usernameObj = str(obj.username)
        print(user.username == usernameObj)
        return user.username == usernameObj
