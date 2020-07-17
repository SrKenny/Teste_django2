from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Categories, Products


class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    label = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='categories-detail')
    class Meta:
        model = Categories
        fields = ('label', 'type', 'rank', 'image', 'timestamp')

class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.SlugRelatedField(queryset=Categories.objects.all(), slug_field='label')
    class Meta:
        model = Products
        fields = ('pk', 'category', 'title', 'name', 'description', 'image', 'timestamp')
