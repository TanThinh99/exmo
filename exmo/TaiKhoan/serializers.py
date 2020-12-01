from rest_framework import serializers

from .models import Taikhoan

class TaiKhoanSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Taikhoan
        fields = ('matk', 'username', 'password', 'hoten', 'diachi', 'sodienthoai')

    def create(self, validated_data):
        userObj = Taikhoan(
            username = validated_data['username'],
            hoten = validated_data['hoten'],
            diachi = validated_data['diachi'],
            sodienthoai = validated_data['sodienthoai'],
            isadmin = 0
        )
        userObj.set_password(validated_data['password'])
        userObj.save()
        return userObj

    def update(self, instance, validated_data):
        username = validated_data.get('username', instance.username)
        userObj = Taikhoan.objects.get(username=username)
        userObj.hoten = validated_data['hoten']
        userObj.diachi = validated_data['diachi']
        userObj.sodienthoai = validated_data['sodienthoai']

        if validated_data['password'] != '@':
            userObj.set_password(validated_data['password'])

        userObj.save()
        return userObj


class GrantPermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Taikhoan
        fields = ['isadmin']