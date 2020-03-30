from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ProductsSerializer, CategoriesSerializer
from .models import Categories, Products

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



