from elasticsearch_dsl.connections import connections

from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Document, Text, Date, Float, Search

from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models

connections.create_connection()


class ProductIndex(Document):
    category = Text()
    name = Text()
    title = Text()
    timestamp = Date()
    description = Text()
    price = Float()

    class Meta:
        index = 'products-index'


def bulk_indexing():
    ProductIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in models.Products.objects.all().iterator()))


def search(name):
    s = Search().filter('term', name=name)
    response = s.execute()
    return response

