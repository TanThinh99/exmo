from rest_framework import serializers

from .models import Nhomhanghoa

class NhomHangHoaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nhomhanghoa
        fields = ['manhom', 'ten']