from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Costume(models.Model):
    costume_name = models.TextField(max_length=30)
    costume_about = models.TextField(max_length=300)
    costume_count = models.IntegerField()
    costume_price = models.IntegerField()
    costume_image = models.ImageField(upload_to='costume_images/')

#
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     fname = models.TextField(max_length=50)
#     lname = models.TextField(max_length=50)
