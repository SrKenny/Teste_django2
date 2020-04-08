from django.shortcuts import render
from rest_framework import viewsets, filters, generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import ProductsSerializer, CategoriesSerializer
from .models import Categories, Products

#View da Categoria

class CategoriesList(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    name = 'categories-list'
    #filter_backends = [filters.SearchFilter]
    #search_fields = ['label', 'type']

class CategoriesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    name = 'categories-detail'

#View do Produto
class ProductsList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    name = 'products-list'
    #filter_backends = [filters.SearchFilter]
    #search_fields = ['name', 'title', 'category']

class ProductsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    name = 'products-detail'


