from django.db import models
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/')
    price = models.IntegerField()  
    description = models.TextField()
    sales = models.IntegerField(default=0)

    def __str__(self):
        return self.name

# class Lottery(models.Model):
# name = models.CharField(max_length=100)
# description = models.TextField()
# points_required = models.IntegerField(default=0)

# def __str__(self):
#    return self.name


# Create your models here.
