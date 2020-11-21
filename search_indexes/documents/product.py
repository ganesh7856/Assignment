from django.conf import settings
from django_elasticsearch_dsl import Document, Index, fields
from elasticsearch_dsl import analyzer

from products.models import Product

# Name of the Elasticsearch index
PRODUCT_INDEX = Index('product')

# See Elasticsearch Indices API reference for available settings
PRODUCT_INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)

html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    bool=["standard", "lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)


@PRODUCT_INDEX.doc_type
class ProductDocument(Document):
    """Products Elasticsearch document."""

    id = fields.IntegerField(attr='id')

    name = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )


    slug = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )


    description = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )


    category = fields.TextField(
        attr='category',
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )

    price = fields.FloatField()

    quantity = fields.FloatField()

    class Django(object):
        """Inner nested class Django."""

        model = Product  # The model associate with this Documente


# @INDEX.doc_type
# class CategoryDocument(Document):
#     """Book Elasticsearch document."""
#
#     id = fields.IntegerField(attr='id')
#
#     name = fields.TextField(
#         analyzer=html_strip,
#         fields={
#             'raw': fields.TextField(analyzer='keyword'),
#         }
#     )
#
#     class Django(object):
#         """Inner nested class Django."""
#
#         model = Product  # The model associate with this Documente
