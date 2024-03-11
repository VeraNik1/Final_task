from django.template.context_processors import static
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('registration/', views.registration, name='registration'),
    path('login/', auth_views.LoginView.as_view(next_page='/'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('show_five_recipes/', views.show_five_recipes, name='show_five_recipes'),
    path('show_recipe/<int:recipe_id>', views.show_the_recipe, name='show_the_recipe'),
    path('edit_recipe/<int:recipe_id>', views.edit_recipe, name='edit_recipe'),
    path('show_all_my_recipes/', views.show_all_my_recipes, name='show_all_my_recipes'),
    path('delete_recipe/<int:recipe_id>', views.delete_recipe, name='delete_recipe'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)