from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('recipe/<int:id>/', views.recipe_info, name='recipe'),
    path('add-recipe/', views.add_recipe, name='add_recipe'),
    path('recipe/<int:id>/edit/', views.edit_recipe, name='edit_recipe'),
    path('recipe/<int:id>/delete/', views.del_recipe, name='edit_recipe'),
    path('category/', views.list_category, name='lst_category'),
    path('category/<int:pk>', views.get_category, name='category'),
    path('my-recipes/', views.my_recipes, name='my_recipes'),
]
