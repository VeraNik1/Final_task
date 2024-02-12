from django.urls import path
from . import views


urlpatterns = [
 path('', views.index, name='index'),
 path('clothes/', views.clothes, name='clothes'),
 path('footwear/', views.footwear, name='footwear'),
 path('jacket/', views.jacket, name='jacket'),
]