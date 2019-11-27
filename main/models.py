from django.db import models


# Create your models here.

class Costume(models.Model):
    costume_name = models.TextField(max_length=30)
    costume_about = models.TextField(max_length=300)
    costume_count = models.IntegerField()
    costume_price = models.IntegerField()
    costume_image = models.ImageField(upload_to='costume_images/')
