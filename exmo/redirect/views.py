from django.shortcuts import render

from NhomHangHoa.serializers import NhomHangHoaSerializer
from NhomHangHoa.models import Nhomhanghoa

from HangHoa.serializers import HangHoaSerializer
from HangHoa.models import Hanghoa

# Create your views here.

def Index(request):
    nhomHangHoa = Nhomhanghoa.objects.all()
    nhomHangHoaArr = NhomHangHoaSerializer(nhomHangHoa, many=True)

    hangHoa = Hanghoa.objects.all()
    hangHoaArr = HangHoaSerializer(hangHoa, many=True)
    return render(request, 'user/index.html', {'nhomHangHoaArr': nhomHangHoaArr.data, 'hangHoaArr': hangHoaArr.data})


def Contact(request):
    return render(request, 'user/Contact.html')


def Login(request):
    return render(request, 'user/login.html')


def Product(request, product_key):
    hangHoa = Hanghoa.objects.get(pk=product_key)
    nhomHangHoa = Nhomhanghoa.objects.get(pk=hangHoa.manhom.manhom)
    nhomHangHoaArr = Nhomhanghoa.objects.all()
    data = {
        'hangHoa': hangHoa,
        'nhomHangHoa': nhomHangHoa,
        'nhomHangHoaArr': nhomHangHoaArr
    }
    return render(request, 'user/product.html', data)


def Register(request):
    return render(request, 'user/register.html')


def Shop(request):
    return render(request, 'user/shop.html')


def ShoppingCart(request):
    return render(request, 'user/shopping-cart.html')


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