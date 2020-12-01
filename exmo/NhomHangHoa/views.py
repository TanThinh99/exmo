from django.shortcuts import render
from django.http import Http404

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import NhomHangHoaSerializer
from .models import Nhomhanghoa
from .permissions import IsAdmin

from HangHoa.models import Hanghoa
from HangHoa.serializers import HangHoaSerializer

# Create your views here.

class NhomHangHoaList(generics.ListAPIView):
    queryset = Nhomhanghoa.objects.all()
    serializer_class = NhomHangHoaSerializer
    permission_classes = [AllowAny]


class NhomHangHoaCreate(generics.CreateAPIView):
    queryset = Nhomhanghoa.objects.all()
    serializer_class = NhomHangHoaSerializer
    permission_classes = [IsAuthenticated, IsAdmin]


class NhomHangHoaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nhomhanghoa.objects.all()
    serializer_class = NhomHangHoaSerializer
    permission_classes = [IsAuthenticated, IsAdmin]


class HasHangHoa(APIView):
    permission_classes = [AllowAny]

    def get_object(self, pk):
        try:
            return Nhomhanghoa.objects.get(pk=pk)
        except Nhomhanghoa.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        nhomHangHoa = self.get_object(pk)
        hangHoa = Hanghoa.objects.filter(manhom=nhomHangHoa)
        serializer = HangHoaSerializer(hangHoa, many=True)
        return Response(serializer.data)
