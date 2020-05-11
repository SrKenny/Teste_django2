from django.shortcuts import render
from .documents import ProductsDocument

# Create your views here.

def search(request):
    q = request.GET.get('q')
    if q:
        products = ProductsDocument.search().query("match", name=q)
    else:
        products = ''
    
    return render(request, 'search/search.html', {'products': products})
