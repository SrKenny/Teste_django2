from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Categories, Products


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'label', 'image', ]

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'category', 'name', 'description', 'image']
