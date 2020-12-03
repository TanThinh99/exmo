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