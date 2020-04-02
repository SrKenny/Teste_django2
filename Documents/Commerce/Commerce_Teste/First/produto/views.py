from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework import permissions
from .serializers import ProductsSerializer, CategoriesSerializer
from .models import Categories, Products

#View da Categoria

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['label', 'type']
    ordering_fields = []
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#View do Produto

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'title', 'category']
    ordering_fields = []
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



