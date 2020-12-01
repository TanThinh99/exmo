from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import TaiKhoanSerializer, GrantPermissionSerializer
from .models import Taikhoan
from .permissions import IsAdmin, IsOwnerUser

# Create your views here.

class TaiKhoanList(generics.ListAPIView):
    queryset = Taikhoan.objects.all()
    serializer_class = TaiKhoanSerializer
    permission_classes = [IsAuthenticated, IsAdmin]


class TaiKhoanCreate(generics.CreateAPIView):
    queryset = Taikhoan.objects.all()
    serializer_class = TaiKhoanSerializer
    permission_classes = [AllowAny]


class TaiKhoanDetailUpdate(generics.RetrieveUpdateAPIView):
    queryset = Taikhoan.objects.all()
    serializer_class = TaiKhoanSerializer
    permission_classes = [IsAuthenticated, IsOwnerUser]


class TaiKhoanDelete(generics.DestroyAPIView):
    queryset = Taikhoan.objects.all()
    serializer_class = TaiKhoanSerializer
    permission_classes = [IsAuthenticated, IsAdmin]


class GrantPermission(generics.UpdateAPIView):
    queryset = Taikhoan.objects.all()
    serializer_class = GrantPermissionSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
