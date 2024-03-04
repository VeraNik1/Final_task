from django.urls import path
from .views import *

urlpatterns = [
    path('orders/<int:user_id>', ClientOrders.as_view(), name='client_statistics'),
    path('products/<int:user_id>', OrderedProducts.as_view(), name='orders_statistics'),
    path('', index, name='index'),
    path('index/', index),
    path('product/<int:product_id>/edit', edit_product, name='edit_product'),
    path('users/', users_view),
    path('products/', products_view),
    path('orders/', orders_view),
    path('order/<int:order_id>/', get_order_view, name='get_order_view'),
    path('product/<int:product_id>/', get_product_view, name='get_product_view'),
    path('user/<int:user_id>/', get_user_view, name='get_user_view'),
]