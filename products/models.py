from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

class Category(models.Model):
    CategoryName =  models.CharField(max_length=100, unique=True)
    CategoryDescription = models.CharField(max_length=300)


class Product(models.Model):
    ProductName = models.CharField(max_length=150)
    ProductCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    ProductDescription = models.CharField(max_length=500)
    ProductImage = models.ImageField(upload_to="Products/Images/", blank=True, null=True)
    ProductQuantity = models.IntegerField()
    ProductPrice = models.DecimalField(max_digits=10, decimal_places=2)
    ProductCreated_at = models.DateTimeField(auto_now_add=True)
