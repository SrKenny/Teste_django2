from django.shortcuts import render
from rest_framework import generics
from django.views.generic import ListView
from .serializers import ProductsSerializer, CategoriesSerializer
from .models import Categories, Products


class ProductView(ListView):
    model = Products
    template_name = 'products.html'


# View da Categoria

class CategoriesList(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    name = 'categories-list'
    filter_fields = ('label',)
    search_fields = ('^label',)
    ordering_fields = ('label',)


# class CategoriesDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Categories.objects.all()
#     serializer_class = CategoriesSerializer
#     name = 'categories-detail'

# View do Produto
class ProductsList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    name = 'products-list'
    filter_fields = ('name', 'category',)
    search_fields = ('^name',)
    ordering_fields = ('name', 'timestamp',)
    template_name = 'products.html'


class ProductsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    name = 'products-detail'
