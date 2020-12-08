from rest_framework import serializers

from .models import Donhang

class DonHangSerializer(serializers.ModelSerializer):

    class Meta:
        model = Donhang
        fields = ['madh', 'thoigiandathang', 'trangthai', 'manv', 'makh', 'hoten', 'diachi', 'sodienthoai']
