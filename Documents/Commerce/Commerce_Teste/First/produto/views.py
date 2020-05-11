from django.shortcuts import render
from rest_framework import viewsets, filters, generics
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import ProductsSerializer, CategoriesSerializer
from .models import Categories, Products

#View da Categoria

class CategoriesList(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    name = 'categories-list'
    filter_fields = ('label',)
    search_fields = ('^label',)
    ordering_fields = ('label',)

class CategoriesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    name = 'categories-detail'

#View do Produto
class ProductsList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    name = 'products-list'
    filter_fields = ('name', 'category',)
    search_fields = ('^name',)
    ordering_fields = ('name', 'timestamp',)

class ProductsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    name = 'products-detail'


