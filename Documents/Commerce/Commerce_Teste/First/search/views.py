from django.shortcuts import render
from .documents import ProductsDocument
from elasticsearch import Elasticsearch


# Create your views here.

def search(request):
    q = request.GET.get('q')
    if q:
        products = ProductsDocument.search().query("match", name=q)
    else:
        products = ''

    return render(request, 'search/search.html', {'products': products})


es1 = {
    "name": "Django Book",
    "description": "Good Book",
    "price": "250"
}


def suggestion(request):
    es = Elasticsearch()
    es.index(index='products-index', id=4, body=es1)
    test = es.get(index='products-index', id=1)
    print(test)
    es.search(
        index='products-index',
        body={
            "query": {
                "term": {"title": "fini"}
            },
            "aggs": {
                "recommendations": {
                    "significant_terms": {
                        "field": "title",
                        "exclude": "fini",
                    }
                }
            }

        }
    )

    return render(request, 'search/suggestion.html', {'suggest': es})
