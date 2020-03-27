from django.shortcuts import render

def products(request):
    return render(request, 'first/products.html', {})

def categories(request):
    return render(request, 'first/categories.html', {})
