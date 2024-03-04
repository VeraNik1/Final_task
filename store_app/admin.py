from django.contrib import admin
from django.urls import reverse
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'reg_date']
    list_filter = ['name', 'reg_date']
    list_sort = ['id', 'name', 'reg_date']
    fieldsets = [('Общие данные:',
                  {'classes': ['wide'],
                   'fields': ['name', 'phone', 'reg_date'],
                   },
                  ),
                 ('Подробности:',
                  {'classes': ['collapse'],
                   'description': 'Полная информация',
                   'fields': ['email', 'address'],
                   },
                  ),
                 ]
    readonly_fields = ['id', 'reg_date']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_filter = ['price', 'name']
    list_sort = ['id', 'name', 'price']
    fieldsets = [('Общие данные:',
                    {'classes': ['wide'],
                     'fields': ['name', 'price'],
                    },
                ),
                ('Подробности:',
                    {'classes': ['collapse'],
                     'description': 'Полная информация',
                     'fields': ['description', 'quantity', 'image'],
                    },
                ),
            ]
    readonly_fields = ['id']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'total_price']
    list_filter = ['customer', 'products']
    list_sort = ['id', 'customer', 'total_price', 'order_date']
    fieldsets = [('Общие данные:',
                    {'classes': ['wide'],
                     'fields': ['customer', 'total_price'],
                    },
                ),
                ('Подробности:',
                    {'classes': ['collapse'],
                     'description': 'Полная информация',
                     'fields': ['products', 'order_date'],
                    },
                ),
            ]
    readonly_fields = ['id', 'order_date']
