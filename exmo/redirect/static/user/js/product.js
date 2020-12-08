document.getElementById('addCartBtn').onclick = function() {
    var maHangHoa = document.getElementById('maHangHoa').innerHTML *1;
    var soLuong = document.getElementById('soluong').value *1;
    var soLuongConLai = document.getElementById('soluongconlai').innerHTML *1;
    if((soLuong > 0) && (soLuong <= soLuongConLai))
    {
        $.get('addCart', {
            'maHangHoa': maHangHoa,
            'soLuong': soLuong,
            'soLuongConLai': soLuongConLai
        }, function(data) {
            alert('Đã thêm vào giỏ hàng');
        });
    }
    else
    {
        alert('Số lượng thêm vào phải lớn hơn 0 và nhỏ hơn hoặc bằng '+ soLuongConLai +'!!');
    }
}