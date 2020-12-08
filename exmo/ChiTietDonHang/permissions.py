from rest_framework.permissions import BasePermission

from DonHang.models import Donhang

class IsOwnerAndDoNotPass(BasePermission):

    def has_permission(self, request, view):
        data = request.data
        madh = data.get('madh')
        donHang = Donhang.objects.get(pk=madh)
            # makh (donHang.makh: return Taikhoan object)
        makh = donHang.makh
        return (donHang.trangthai == 0) & (str(makh) == str(request.user))
