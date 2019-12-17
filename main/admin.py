from django.contrib import admin
from .models import Costume, Cart, FinishedOrders


# Register your models here.


class CostumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_name', 'item_quantity', 'item_price')


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_name', 'item_items', 'item_cost')


class FinishedOrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_name', 'item_items', 'item_cost', 'item_date')


admin.site.register(Cart, CartAdmin)
admin.site.register(Costume, CostumeAdmin)
admin.site.register(FinishedOrders, FinishedOrdersAdmin)
