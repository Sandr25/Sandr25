from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING)

class Essential_Oil(models.Model):
    name = models.CharField(max_length=255)
    latin_name = models.CharField(max_length=255)
    ingredients = models.CharField(max_length=255)
    plant_part = models.CharField(max_length=255, default='flower')
    capacity = models.IntegerField()
    origin_country = models.CharField(max_length=255)
    extraction_method = models.CharField(max_length=255)
    quality_control = models.CharField(max_length=255)
    batch_number = models.IntegerField()
    product = models.OneToOneField('Product', on_delete=models.CASCADE)

class Candle(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255, default='white')
    capacity = models.IntegerField(default=120)
    product = models.OneToOneField('Product', on_delete=models.CASCADE)

class Gift_Card(models.Model):
    name = models.CharField(max_length=255)
    product = models.OneToOneField('Product', on_delete=models.CASCADE)

class Difussor(models.Model):
    name = models.CharField(max_length=255)
    specifications = models.CharField(max_length=255)
    features = models.CharField(max_length=255)
    product = models.OneToOneField('Product', on_delete=models.CASCADE)

class User_Product(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey('Product', on_delete=models.DO_NOTHING)
    order = models.ForeignKey('Order', on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=255)
    status = models.ForeignKey('Status', on_delete=models.DO_NOTHING)

class Profile(models.Model):
    address = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Status(models.Model):
    name = models.CharField(max_length=255)


