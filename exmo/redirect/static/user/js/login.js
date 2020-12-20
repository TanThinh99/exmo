document.getElementById('submitBtn').onclick = function() {
    var check = true;
    var username = document.getElementById('username').value;
    if(username == '')
    {
        document.getElementById('usernameError').style.display = 'block';
        check = false;
    }
    else
    {
        document.getElementById('usernameError').style.display = 'none';
    }

    var password = document.getElementById('pass').value;
    if(password == '')
    {
        document.getElementById('passwordError').style.display = 'block';
        check = false;
    }
    else
    {
        document.getElementById('passwordError').style.display = 'none';
    }
    if( check )
    {
        axios({
            method: 'POST',
            url: 'http://localhost:8000/api/token/',
            data: {
                'username': username,
                'password': password
            }
        })
        .then(function(response) {
            $.get('saveAccess', {
                'username': username,
                'access': response.data.access                
            }, function(data) {
                window.location.href = 'http://localhost:8000/';
            });            
        })
        .catch(function(error) {
            alert('Đăng nhập thất bại');
            console.log(error);
        });
    }
}

// admin
    //duyet don hang
$.get('getAccess', function(data) {
    var access = data;
    var donHangId;
    axios({
        method: 'PUT',
        url: 'http://localhost:8000/donhang/pass/'+ donHangId,
        headers: {
            'Authorization': 'Bearer '+ access
        }
    })
    .then(function(data) {
        alert('Duyệt đơn hàng thành công');
    })
    .catch(function(error) {
        console.log(error);
    });
});

    // Tao san pham
$.get('getAccess', function(data) {
    var access = data;
    var myFile = document.getElementById('myFile').files[0];
    var ten;
    var moTa;
    var gia;
    var soLuong;
    var maNhom;

    var formData = new FormData();
    if(myFile != undefined)
    {
        formData.append('hinhanh', myFile);
    }
    formData.append('ten', ten);
    formData.append('mota', moTa);
    formData.append('gia', gia);
    formData.append('soluong', soLuong);
    formData.append('manhom', maNhom);  

    axios({
        method: 'POST',
        url: 'http://localhost:8000/hanghoa/create',
        data: formData,
        headers: {
            'Authorization': 'Bearer '+ access
        }
    })
    .then(function(data) {
        alert('Tạo hàng hóa thành công');
    })
    .catch(function(error) {
        console.log(error);
    });
});

    // Tao nhom hang hoa
$.get('getAccess', function(data) {
    var access = data;
    var ten;
    axios({
        method: 'POST',
        url: 'http://localhost:8000/nhomhanghoa/create',
        data: {
            ten: ten
        },
        headers: {
            'Authorization': 'Bearer '+ access
        }
    })
    .then(function(data) {
        alert('Tạo nhóm hàng hóa thành công');
    })
    .catch(function(error) {
        console.log(error);
    });
});

    // gan quyen
$.get('getAccess', function(data) {
    var access = data;
    var grant;
    var userid;
    axios({
        method: 'PUT',
        url: 'http://localhost:8000/taikhoan/grantPermission/'+ userid,
        data: {
            isadmin: grant
        },
        headers: {
            'Authorization': 'Bearer '+ access
        }
    })
    .then(function(data) {})
    .catch(function(error) {
        console.log(error);
    });
});