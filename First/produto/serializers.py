from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Categories, Products


class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'label']

class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'category', 'name', 'description', 'image']
