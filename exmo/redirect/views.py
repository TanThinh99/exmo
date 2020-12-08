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
    for item in hangHoaArr:
        money = ShowMoney(str(item.gia))
        item.gia = money

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
    hangHoa.gia = ShowMoney(str(hangHoa.gia))
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
    user = ''
    try:
        username = request.session['username']
        user = Taikhoan.objects.get(username=username)
        name = user.hoten
    except KeyError:
        pass
    
    try:
        count = request.session['count']
    except KeyError:
        count = 0
    sttArr = []
    productArr = []
    amountArr = []
    moneyArr = []
    moneyTotal = 0
    for i in range(0, count):
        i = str(i)
            # STT
        sttArr.append(int(i) + 1)
            # product
        prID = request.session['pr'+i]
        hangHoa = Hanghoa.objects.get(pk=prID)
            # amount
        amount = request.session['amo'+i]
        amountArr.append(amount)
            # money
        money = int(hangHoa.gia) * amount
        moneyArr.append(ShowMoney(str(money)))
            # moneyTotal
        moneyTotal += money
            # product money
        hangHoa.gia = ShowMoney(str(hangHoa.gia))
        productArr.append(hangHoa)
    bill = zip(sttArr, productArr, amountArr, moneyArr)

    data = {
        'nameOfUser': name,
        'user': user,
        'bill': bill,
        'moneyTotal': ShowMoney(str(moneyTotal)),
        'amountOfProduct': count
    }
    return render(request, 'user/shopping-cart.html', data)


def ShowMoney(money):
    if len(money) > 3:
        string = ''
        while len(money) > 3:
            temp = money[len(money)-3:]
            string = '.'+ temp + string
            money = money[0:len(money)-3]
        return money + string
    return money


    #============================== AJAX =====================================#
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
        return redirect('http://localhost:8000/')
    return render(request, "user/accessUserAjax.html", {'access': access})


def AddCart(request):
    maHangHoa     = int(request.GET.get('maHangHoa'))
    soLuong       = int(request.GET.get('soLuong'))
    soLuongConLai = int(request.GET.get('soLuongConLai'))
    try:
        count = request.session['count']
    except KeyError:
        count = 0
        request.session['count'] = 0
    found = False
    for i in range(0, count):
        i = str(i)
        prID = request.session['pr'+i]
        if prID == maHangHoa:
            if (request.session['amo'+i] + soLuong) > soLuongConLai:
                request.session['amo'+i] = soLuongConLai
            else:  
                request.session['amo'+i] += soLuong
            found = True
            break
        
    if not found:
        request.session['pr'+str(count)] = maHangHoa
        request.session['amo'+str(count)] = soLuong
        count += 1
        request.session['count'] = count
    return render(request, 'user/accessUserAjax.html')


def DeleteProductFromCart(request):
    mahh = int(request.GET.get('mahh'))
    try:
        count = request.session['count']
    except KeyError:
        return redirect('http://localhost:8000/')

    for i in range(0, count):
        i = str(i)
        mahhSession = request.session['pr'+i]
        if mahhSession == mahh:
            for j in range(int(i), count-1):
                request.session['pr'+str(j)] = request.session['pr'+str(j+1)]
                request.session['amo'+str(j)] = request.session['amo'+str(j+1)]
            break
    
    request.session['count'] = count - 1
    return render(request, 'user/accessUserAjax.html')


def DeleteCart(request):
    count = 0
    try:
        count = request.session['count']
    except KeyError:
        pass
    for i in range(0, count):
        i = str(i)
        del request.session['pr'+str(i)]
        del request.session['amo'+str(i)]
    del request.session['count']
    return render(request, 'user/accessUserAjax.html')


def TestSessionForCart(request):
    print('Run test session for cart')
    count = 0
    try:
        count = request.session['count']
    except KeyError:
        pass
    print(count)
    for i in range(0, count):
        print(str(request.session['pr'+str(i)]) +', '+ str(request.session['amo'+str(i)]))
        
        # delete all session for cart
    # print('delete all session for cart')
    # count = 0
    # try:
    #     count = request.session['count']
    # except KeyError:
    #     pass
    # for i in range(1, count+1):
    #     del request.session['pr'+str(i)]
    #     del request.session['amo'+str(i)]
    # del request.session['count']