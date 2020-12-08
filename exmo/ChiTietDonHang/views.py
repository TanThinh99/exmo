from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Chitietdonhang
from .serializers import ChitietdonhangSerializer
from .permissions import IsOwnerAndDoNotPass

# Create your views here.

class ChiTietDonHangCreate(generics.CreateAPIView):
    queryset = Chitietdonhang.objects.all()
    serializer_class = ChitietdonhangSerializer
    permission_classes = [IsAuthenticated, IsOwnerAndDoNotPass]