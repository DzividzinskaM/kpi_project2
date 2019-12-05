from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField


# Create your models here.

class Costume(models.Model):
    name = models.TextField(max_length=100)
    about = models.TextField(max_length=300)
    count = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='static/img/')

    def __str__(self):
        return f'{self.name} {self.count} {self.price}'


class Cart(models.Model):
    user = models.TextField(max_length=30)
    items = JSONField(default=dict)
    cost = models.IntegerField()

    def __str__(self):
        return f'{self.user} {self.items} {self.cost}'
