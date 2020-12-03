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
]