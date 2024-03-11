from django.contrib import admin
from .models import *


@admin.register(Author)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'cooking_time', 'author']
    list_filter = ['name', 'time_create', 'category', 'author']
    list_sort = ['id', 'name', 'author']
    fieldsets = [('Main data:',
                  {'classes': ['wide'],
                   'fields': ['name', 'category', 'author'],
                   },
                  ),
                 ('More:',
                  {'classes': ['collapse'],
                   'description': 'description',
                   'fields': ['description', 'cooking_time', 'cooking_steps', 'image'],
                   },
                  ),
                 ]
    readonly_fields = ['id']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    readonly_fields = ['id']
