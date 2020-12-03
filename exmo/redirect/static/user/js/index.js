axios({
    method: 'GET',
    url: 'http://localhost:8000/nhomhanghoa/list',
})
.then(function(response) {
    console.log(response);
    typeArr = response.data;
    var str = '';
    for(item of typeArr)
    {console.log(item.ten);
        str += '<section class="women-banner spad">\
                    <div class="container-fluid">\
                        <div class="row">\
                            <div class="col-lg-3">\
                                <div class="product-large set-bg" data-setbg="{% static \'img/baoda2.jpg\' %}">\
                                    <h2>'+ item.ten +'</h2>\
                                    <a href="#">Xem nhiều sản phẩm khác</a>\
                                </div>\
                            </div>\
                            <div class="col-lg-8 offset-lg-1">\
                                <div class="filter-control">\
                                    <ul>\
                                        <li class="active">'+ item.ten +'</li>\
                                    </ul>\
                                </div>\
                                <div class="product-slider owl-carousel" id="type'+ item.manhom +'">';
                                axios({
                                    method: 'GET',
                                    url: 'http://localhost:8000/nhomhanghoa/hasHangHoa/'+ item.manhom
                                })
                                .then(function(response) {
                                    console.log(response);
                                    productArr = response.data;
                                    var str2 = '';
                                    for(productItem of productArr)
                                    {//console.log(productItem.ten);
                                        str2 += '<div class="product-item">\
                                                    <div class="pi-pic">\
                                                        <img src="'+ productItem.hinhanh +'" alt="">\
                                                        <!-- <div class="icon">\
                                                            <i class="icon_heart_alt"></i>\
                                                        </div> -->\
                                                        <ul>\
                                                            <!-- <li class="w-icon active"><a href="#"><i class="icon_bag_alt"></i></a></li> -->\
                                                            <li class="quick-view"><a href="product.php">+ Xem nhanh</a></li>\
                                                            <!-- <li class="w-icon"><a href="#"><i class="fa fa-random"></i></a></li> -->\
                                                        </ul>\
                                                    </div>\
                                                    <div class="pi-text">\
                                                        <div class="catagory-name">Ốp lưng</div>\
                                                        <a href="#">\
                                                            <h5>'+ productItem.ten +'</h5>\
                                                        </a>\
                                                        <div class="product-price">\
                                                        '+ productItem.gia +' vnd\
                                                        </div>\
                                                    </div>\
                                                </div>';console.log(productItem.manhom.ten);
                                    }
                                    document.getElementById('type'+ productItem.manhom).innerHTML = str2;
                                })
                                .catch(function(error) {
                                    
                                });
                                    
                        str += '</div>\
                            </div>\
                        </div>\
                    </div>\
                </section>';
    }
    document.getElementById('mainContent').innerHTML = str;
})
.catch(function(error) {
    console.log(error);
});

{/* <section class="women-banner spad">
    <div class="container-fluid">
        <div class="row">
            <div class="col-lg-3">
                <div class="product-large set-bg" data-setbg="{% static 'img/baoda2.jpg' %}">
                    <h2>Bao da - Ốp lưng</h2>
                    <a href="#">Xem nhiều sản phẩm khác</a>
                </div>
            </div>
            <div class="col-lg-8 offset-lg-1">
                <div class="filter-control">
                    <ul>
                        <li class="active">Bao da - Ốp lưng cao cấp</li>
                    </ul>
                </div>
                <div class="product-slider owl-carousel">
                        <div class="product-item">
                            <div class="pi-pic">
                                <img src="{% static 'img/baoda1.jpg' %}" alt="">
                                <!-- <div class="icon">
                                    <i class="icon_heart_alt"></i>
                                </div> -->
                                <ul>
                                    <!-- <li class="w-icon active"><a href="#"><i class="icon_bag_alt"></i></a></li> -->
                                    <li class="quick-view"><a href="product.php">+ Xem nhanh</a></li>
                                    <!-- <li class="w-icon"><a href="#"><i class="fa fa-random"></i></a></li> -->
                                </ul>
                            </div>
                            <div class="pi-text">
                                <div class="catagory-name">Ốp lưng</div>
                                <a href="#">
                                    <h5>Ốp lưng Spigen Ultra Hybrid Iphone 12</h5>
                                </a>
                                <div class="product-price">
                                540.000 vnd
                                </div>
                            </div>
                        </div>    
                                    
                </div>
            </div>
        </div>
    </div>
</section> */}