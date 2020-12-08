from django.shortcuts import render
from django.http import Http404

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Donhang
from .serializers import DonHangSerializer
from .permissions import IsAdmin, IsAdminOrOwnerUser

from TaiKhoan.models import Taikhoan
from ChiTietDonHang.serializers import ChitietdonhangSerializer

# Create your views here.

class DonHangList(generics.ListAPIView):
    queryset = Donhang.objects.all()
    serializer_class = DonHangSerializer
    permission_classes = [IsAuthenticated, IsAdmin]


class DonHangCreate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        data = request.data
        donHang = Donhang(
            makh = request.user,
            manv = Taikhoan.objects.get(pk=3),
            hoten = data.get('hoten'),
            diachi = data.get('diachi'),
            sodienthoai = data.get('sodienthoai')
        )
        donHang.save()
        serializer = DonHangSerializer(donHang)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DonHangDetail(generics.RetrieveAPIView):
    queryset = Donhang.objects.all()
    serializer_class = DonHangSerializer
    permission_classes = [IsAuthenticated, IsAdminOrOwnerUser]


class DonHangDelete(APIView):
    permission_classes = [IsAuthenticated, IsAdminOrOwnerUser]

    def get_object(self, pk):
        try:
            donHang = Donhang.objects.get(pk=pk)
            self.check_object_permissions(self.request, donHang)
            return donHang
        except Donhang.DoesNotExist:
            return Http404

    def delete(self, request, pk, format=None):
        donHang = self.get_object(pk)
        if donHang.trangthai == 0:
            detailList = donHang.chitietdonhang_set.all()
            for item in detailList:
                item.delete()

            donHang.delete()
            return Response({"error": ""}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Bill is pass"}, status=status.HTTP_200_OK)


class HasChiTietDonHang(APIView):
    permission_classes = [IsAuthenticated, IsAdminOrOwnerUser]

    def get_object(self, pk):
        try:
            donHang = Donhang.objects.get(pk=pk)
            self.check_object_permissions(self.request, donHang)
            return donHang
        except Donhang.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        donHang = self.get_object(pk)
        chiTietList = donHang.chitietdonhang_set.all()
        serializer = ChitietdonhangSerializer(chiTietList, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)