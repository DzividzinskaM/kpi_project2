from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField


# Create your models here.

class Costume(models.Model):
    costume_name = models.TextField(max_length=30)
    costume_about = models.TextField(max_length=300)
    costume_count = models.IntegerField()
    costume_price = models.IntegerField()
    costume_image = models.ImageField(upload_to='static/img/')

    def __str__(self):
        return f'Назва: =={self.costume_name}\n==; ' \
               f'Кількість: {self.costume_count}'


class Cart(models.Model):
    user = models.TextField(max_length=30)
    items = models.TextField()
    cost = models.IntegerField()
