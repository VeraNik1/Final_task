from django.urls import path
from .views import *

urlpatterns = [
    path('orders/<int:user_id>', ClientOrders.as_view(), name='client_statistics'),
    path('products/<int:user_id>', OrderedProducts.as_view(), name='orders_statistics'),
    path('', index, name='index'),
    path('product/<int:product_id>/edit', edit_product, name='edit_product'),
]