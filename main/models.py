from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.postgres.fields import JSONField


# Create your models here.

class Costume(models.Model):
    name = models.TextField(max_length=100)
    about = models.TextField(max_length=300)
    count = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='static/img/')

    def __str__(self):
        return f'{self.name},{self.count},{self.price}'

    def item_name(self):
        return self.name

    item_name.short_description = 'Назва'

    def item_quantity(self):
        return self.count

    item_quantity.short_description = 'Кількість'

    def item_price(self):
        return self.price

    item_price.short_description = 'Ціна'


class Cart(models.Model):
    user = models.TextField(max_length=30)
    items = JSONField(default=dict)
    cost = models.IntegerField()

    def __str__(self):
        return f'{self.user} {self.items} {self.cost}'

    def item_name(self):
        return self.user

    item_name.short_description = 'Клієнт'

    def item_items(self):
        return self.items

    item_items.short_description = 'Корзина'

    def item_cost(self):
        return self.cost

    item_cost.short_description = 'Загальна ціна'
