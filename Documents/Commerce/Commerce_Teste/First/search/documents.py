from django_elasticsearch_dsl import Document, Text, Keyword, fields, Date
from elasticsearch_dsl import InnerDoc, analyzer, tokenizer
from django_elasticsearch_dsl.registries import registry
from products.models import Products

html_strip = analyzer(
    'html_strip',
    tokenizer=tokenizer('trigram', 'nGram', min_gram=3, max_gram=4),
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)


@registry.register_document
class ProductsDocument(Document):
    title = fields.KeywordField()
    name = fields.KeywordField()

    class Index:
        name = 'products-index'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = Products

        fields = [
            'description',
            'price',
            'timestamp',
        ]
