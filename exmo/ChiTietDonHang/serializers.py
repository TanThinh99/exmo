from rest_framework import serializers

from .models import Chitietdonhang

class ChitietdonhangSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chitietdonhang
        fields = ['machitiet', 'mahh', 'madh', 'soluong', 'giadathang']
