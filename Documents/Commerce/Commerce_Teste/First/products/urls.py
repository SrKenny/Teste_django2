from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import ProductView, ProductsList, ProductsDetail, CategoriesList

urlpatterns = [
    path('categories/', CategoriesList.as_view(), name=CategoriesList.name),
    # path('categories/<pk>', views.CategoriesDetail.as_view(), name=views.CategoriesDetail.name),
    path('product/', ProductView.as_view(), name='produtos'),
    path('products/', ProductsList.as_view(), name=ProductsList.name),
    path('products/<pk>', ProductsDetail.as_view(), name=ProductsDetail.name),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)