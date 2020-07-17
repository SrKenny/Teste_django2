from django_elasticsearch_dsl import Document, Text, KeywordField, fields, Date
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
    title = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': KeywordField(),
        },
    )

    name = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': KeywordField(),
        },
    )

    related = fields.TextField(
        fields={
            'raw': KeywordField(multi=True),
        },
        multi=True,
        fielddata=True
    )

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
