from django.urls import path
from . import views

urlpatterns = [
    path('home',views.customer_home,name='image'),
    path('cart',views.customer_cart,name='cart'),
    path('order',views.customer_order,name='order')
]
