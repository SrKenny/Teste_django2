from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoriesList.as_view(), name=views.CategoriesList.name),
    path('categories/<int:id>', views.CategoriesDetail.as_view(), name=views.CategoriesDetail.name),
    path('products/', views.ProductsList.as_views(), name=views.ProductsList.name),
    path('products/<int:id>', views.ProductsDetail.as_view(), name=views.ProductsDetail.name),
]
