from django.urls import path

from . import views

app_name = 'redirect'

urlpatterns = [
    path('', views.Index, name='Index'),
    path('contact', views.Contact, name='Contact'),

    path('login', views.Login, name='Login'),
    path('register', views.Register, name='Register'),
    path('logout', views.Logout, name='Logout'),
    
    path('product/<int:product_key>', views.Product, name='Product'),
    path('shop', views.Shop, name='Shop'),
    path('shoppingCart', views.ShoppingCart, name='ShoppingCart'),

    # AJAX
    path('saveAccess', views.SaveAccess, name='Save_access'),
    path('getAccess', views.GetAccess, name='Get_access'),

        # Cart
    path('product/addCart', views.AddCart, name="Add_cart"),
    path('deleteProduct', views.DeleteProductFromCart, name='Delete_product_from_cart'),
    path('deleteCart', views.DeleteCart, name='Delete_cart'),

    path('TestSessionForCart', views.TestSessionForCart),

    # === ADMIN ====
    path('account', views.AccountList, name='Account_list'),
    path('deal', views.DealList, name='Deal_list'),
    path('product', views.ProductList, name='Product_list'),
    path('addProduct', views.AddProduct, name='Add_product'),
    path('group', views.GroupList, name='Group_list'),
    path('addGroup', views.AddGroup, name='Add_group'),
]