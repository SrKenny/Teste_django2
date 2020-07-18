from django.shortcuts import render
from .documents import ProductsDocument
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q


# Create your views here.

def search(request):
    q = request.GET.get('q')
    products = ProductsDocument.search()
    if q:
       qs = products.query("multi_match", query=q, fields=['title', 'name'])
       # suggest = products.aggs.bucket('recommendations', 'terms', field= "related").metric('max_amt', 'max', field='amount')
    else:
       qs = ''

    suggest = suggestion(q)

    return render(request, 'search/search.html', {'products': qs, 'suggest': suggest})


es1 = {
    "name": "Django Book",
    "description": "Good Book",
    "price": "250"
}


def suggestion(q):
    es = Elasticsearch()
    es.index(index='products-index', id=4, body=es1)
    test = es.get(index='products-index', id=4)
    donut = es.search(
        index='products-index',
        body={
            "query": {
                "match": {"title": q}
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
    return donut
