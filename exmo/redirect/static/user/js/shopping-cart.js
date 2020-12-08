document.getElementById("submitBtn").onclick = function() {
        // Check amount of product in cart
    var proTotal = document.getElementById('amountOfProduct').value *1;
    if(proTotal == 0)
    {
        alert('Bạn không thể thanh toán khi giỏ hàng rỗng');
        return;
    }
    
        // Check logged
    var isLog = document.getElementById('logged').value;
    if(isLog == '')
    {
        alert('Bạn cần đăng nhập để mua hàng!');
        return;
    }

    var check = true;
        // NAME
    var name = document.getElementById('name').value;
    if(name == '')
    {
        document.getElementById('nameError').style.display = 'block';
        check = false;
    }
    else
    {
        document.getElementById('nameError').style.display = 'none';
    }
        // ADDRESS
    var address = document.getElementById('address').value;
    if(address == '')
    {
        document.getElementById('addressError').style.display = 'block';
        check = false;
    }
    else
    {
        document.getElementById('addressError').style.display = 'none';
    }
        // PHONE
    var phone = document.getElementById('phone').value;
    var phoneReg = /^[0-9]{10,11}$/;
    if( phoneReg.test(phone) )
    {
        document.getElementById('phoneError').style.display = 'none';
    }
    else
    {
        document.getElementById('phoneError').style.display = 'block';
        check = false;
    }
    if( check )
    {
        $.get('getAccess', function(data) {
            var access = data;
            axios({
                method: 'POST',
                url: 'http://localhost:8000/donhang/create',
                data: {
                    hoten: name,
                    diachi: address,
                    sodienthoai: phone
                },
                headers: {
                    "Authorization": "Bearer "+ access
                }
            })
            .then(function(response) {
                console.log(response);
                var madh = response.data.madh;
                var amountOfProduct = document.getElementById('amountOfProduct').value *1;
                var str = '';
                for(i=1; i<=amountOfProduct; i++)
                {
                    var mahh = document.getElementById('mahh'+ i).value *1;
                    var amount = document.getElementById('amo'+ i).value *1;
                    var price = document.getElementById('gia'+ i).value *1;
                        // Tạo chi tiết đơn hàng
                    axios({
                        method: 'POST',
                        url: 'http://localhost:8000/chitietdonhang/create',
                        data: {
                            madh: madh,
                            mahh: mahh,
                            soluong: amount,
                            giadathang: price
                        },
                        headers: {
                            "Authorization": "Bearer "+ access
                        }
                    })
                    .then(function(response) {
                        console.log(response);
                    })
                    .catch(function(error) {
                        console.log(error);
                    });
                }
                alert('Tạo đơn hàng thành công!!');
                $.get('deleteCart', function(data){
                    window.location.href = 'http://localhost:8000/shoppingCart';
                });
            })
            .catch(function(error) {
                console.log(error);
            });
        });
    }
}


function DeleteProduct(mahh)
{
    if(confirm('Bạn sẽ bỏ sản phẩm này ra khỏi giỏ hàng?'))
    {
        $.get('deleteProduct', {
            'mahh': mahh
        }, function(data) {
            location.reload();
        })
    }
}
