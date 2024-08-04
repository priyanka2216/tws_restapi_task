from django.urls import path
from .views.home import Index
from .views.login import Login, logout
from .views.signup import Signup
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .views.details import ProductDetail  # Import the new view
from .views.rest_api import TopProductsAPIView
from .middlewares.auth import auth_middleware

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', Cart.as_view(), name='cart'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('update_cart', Cart.as_view(), name='update_cart'),
    path('api/top-products/', TopProductsAPIView.as_view(), name='top-products'),
    path('product/<int:product_id>/', ProductDetail.as_view(), name='product_detail'), 
]
