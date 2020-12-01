from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import HangHoaSerializer
from .permissions import IsAdmin
from .models import Hanghoa

# Create your views here.

class HangHoaList(generics.ListAPIView):
    queryset = Hanghoa.objects.all()
    serializer_class = HangHoaSerializer
    permission_classes = [AllowAny]


class HangHoaCreate(generics.CreateAPIView):
    queryset = Hanghoa.objects.all()
    serializer_class = HangHoaSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
    parser_classes = [MultiPartParser, FormParser]


class HangHoaDetail(generics.RetrieveAPIView):
    queryset = Hanghoa.objects.all()
    serializer_class = HangHoaSerializer
    permission_classes = [AllowAny]


class HangHoaUpdate(generics.UpdateAPIView):
    queryset = Hanghoa.objects.all()
    serializer_class = HangHoaSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
    parser_classes = [MultiPartParser, FormParser]


class HangHoaDelete(generics.DestroyAPIView):
    queryset = Hanghoa.objects.all()
    serializer_class = HangHoaSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
