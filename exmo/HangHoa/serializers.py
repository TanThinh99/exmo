from rest_framework import serializers

from .models import Hanghoa

class HangHoaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hanghoa
        fields = ['mahh', 'ten', 'hinhanh', 'mota', 'gia', 'soluong', 'manhom']