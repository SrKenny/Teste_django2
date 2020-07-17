from django.shortcuts import render
from .documents import ProductsDocument
from elasticsearch import Elasticsearch


# Create your views here.

def search(request):
    q = request.GET.get('q')
    if q:
        products = ProductsDocument.search().query("multi_match", query=q, fields=['title', 'name'])
    else:
        products = ''

    return render(request, 'search/search.html', {'products': products})


es1 = {
    "name": "Django Book",
    "description": "Good Book",
    "price": "250"
}


def suggestion_view(request):
    products = ProductsDocument
    products.search()
    pass

def suggestion(request):
    es = Elasticsearch()
    es.index(index='products-index', id=4, body=es1)
    test = es.get(index='products-index', id=4)
    donut = es.search(
        index='products-index',
        body={
            "query": {
                "match": {"title": "fini"}
            },
            "aggregations": {
                "recommendations": {
                    "terms": {
                        "field": "related",
                        "min_doc_count": 1
                    }
                }
            }

        }
    )
    return render(request, 'search/suggestion.html', {'suggest': donut})
