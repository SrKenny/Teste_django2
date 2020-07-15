from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from produto.models import Products

@registry.register_document
class ProductsDocument(Document):
    class Index:
        name = 'products'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = Products

        fields = [
            'name',
            'description',
            'price',
            'timestamp',
        ]
