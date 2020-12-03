from django.shortcuts import render, redirect

from NhomHangHoa.serializers import NhomHangHoaSerializer
from NhomHangHoa.models import Nhomhanghoa

from HangHoa.serializers import HangHoaSerializer
from HangHoa.models import Hanghoa

from TaiKhoan.models import Taikhoan

# Create your views here.

def Index(request):
    name = ''
    try:
        username = request.session['username']
        user = Taikhoan.objects.get(username=username)
        name = user.hoten
    except KeyError:
        pass

    nhomHangHoaArr = Nhomhanghoa.objects.all()
    hangHoaArr = Hanghoa.objects.all()
    data = {
        'nhomHangHoaArr': nhomHangHoaArr, 
        'hangHoaArr': hangHoaArr,
        'nameOfUser': name
    }
    return render(request, 'user/index.html', data)


def Contact(request):
    name = ''
    try:
        username = request.session['username']
        user = Taikhoan.objects.get(username=username)
        name = user.hoten
    except KeyError:
        pass
    data = {
        'nameOfUser': name
    }
    return render(request, 'user/Contact.html', data)


def Login(request):
    data = {
        'nameOfUser': ''
    }
    return render(request, 'user/login.html', data)


def Register(request):
    data = {
        'nameOfUser': ''
    }
    return render(request, 'user/register.html', data)


def Logout(request):
    try:
        username = request.session['username']
        del request.session['username']
        del request.session['access']
    except KeyError:
        pass
    return redirect('http://localhost:8000/')


def Product(request, product_key):
    name = ''
    try:
        username = request.session['username']
        user = Taikhoan.objects.get(username=username)
        name = user.hoten
    except KeyError:
        pass

    hangHoa = Hanghoa.objects.get(pk=product_key)
    nhomHangHoa = Nhomhanghoa.objects.get(pk=hangHoa.manhom.manhom)
    nhomHangHoaArr = Nhomhanghoa.objects.all()
    data = {
        'hangHoa': hangHoa,
        'nhomHangHoa': nhomHangHoa,
        'nhomHangHoaArr': nhomHangHoaArr,
        'nameOfUser': name
    }
    return render(request, 'user/product.html', data)


def Shop(request):
    name = ''
    try:
        username = request.session['username']
        user = Taikhoan.objects.get(username=username)
        name = user.hoten
    except KeyError:
        pass
    data = {
        'nameOfUser': name
    }
    return render(request, 'user/shop.html', data)


def ShoppingCart(request):
    name = ''
    try:
        username = request.session['username']
        user = Taikhoan.objects.get(username=username)
        name = user.hoten
    except KeyError:
        pass
    data = {
        'nameOfUser': name
    }
    return render(request, 'user/shopping-cart.html', data)


def SaveAccess(request):
    username = request.GET.get('username')
    access = request.GET.get('access')
    request.session['username'] = username
    request.session['access'] = access
    return render(request, "user/accessUserAjax.html")


def GetAccess(request):
    try:
        access = request.session['access']
    except KeyError:
        return redirect('./../')
    return render(request, "user/accessUserAjax.html", {'access': access})