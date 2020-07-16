from django.shortcuts import render
from .documents import ProductsDocument
from elasticsearch import Elasticsearch, RequestsHttpConnection
from aws_requests_auth.boto_utils import BotoAWSRequestsAuth

# Create your views here.

def search(request):
    q = request.GET.get('q')
    products = ProductsDocument.search()
    if q:
        products.query("match", name=q)
    else:
        products.sort('id')

    return render(request, 'search/search.html', {'products': products})


es = Elasticsearch(
  host=host, port=port,
  connection_class=RequestsHttpConnection,
  http_auth=BotoAWSRequestsAuth(),
  scheme=scheme
)
es.search(
  index=index, doc_type=doc_type,
  body={
    "query": {
      "bool": {
        "must": {
          "term": {"products": "apple"}
        }
      }
    },
    "aggs": {
      "recommendations": {
        "significant_terms": {
          "field": "products",
          "exclude": "apple",
          "min_doc_count": 100
        }
      }
    }
  }
)