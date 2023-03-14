from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =  Category
        fields = ('id', 'CategoryName', 'CategoryDescription')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','ProductName', 'ProductCategory', 'ProductDescription', 'ProductImage', 'ProductQuantity', 'ProductPrice', 'ProductCreated_at')


