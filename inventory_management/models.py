from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
   
class Supplier(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    qty_stock = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='images/', blank=True)
    bar_code = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name