document.getElementById('submitBtn').onclick = function() {
    var check = true;
        // username
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

        // name
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

        // password
    var password = document.getElementById('password').value;
    if(password == '')
    {
        document.getElementById('passwordError').style.display = 'block';
        check = false;
    }
    else
    {
        document.getElementById('passwordError').style.display = 'none';
    }

        // password again
    var password2 = document.getElementById('con-pass').value;
    if(password2 != password)
    {
        document.getElementById('passwordError2').style.display = 'block';
        check = false;
    }
    else
    {
        document.getElementById('passwordError2').style.display = 'none';
    }

    if( check )
    {
        var address = document.getElementById('address').value;
        var phone = document.getElementById('phone').value;
        axios({
            method: 'POST',
            url: 'http://localhost:8000/taikhoan/create',
            data: {
                'username': username,
                'password': password,
                'hoten': name,
                'diachi': address,
                'sodienthoai': phone
            }
        })
        .then(function(response) {
            alert('Đăng ký tài khoản thành công!');
            window.location.href = 'http://localhost:8000/login';
        })
        .catch(function(error) {
            console.log(error);
            alert('Đăng ký tài khoản thất bại');
        });
    }
}