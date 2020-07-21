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

# def suggestion(q):
#     client = Elasticsearch()
#
#     s = Search(using=client, index="my-index") \
#         .filter("term", category="search") \
#         .query("match", title="python") \
#
#     s.aggs.bucket('per_tag', 'terms', field='tags') \
#         .metric('max_lines', 'max', field='lines')
#
#     response = s.execute()
#
#     for hit in response:
#         print(hit.meta.score, hit.title)
#
#     for tag in response.aggregations.per_tag.buckets:
#         print(tag.key, tag.max_lines.value)
#     pass

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
