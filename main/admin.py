from django.contrib import admin
from .models import Costume, Cart


# Register your models here.


class CostumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_name', 'item_quantity', 'item_price')


admin.site.register(Cart)
admin.site.register(Costume, CostumeAdmin)
