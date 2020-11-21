from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_TERMS,
    LOOKUP_FILTER_RANGE,
    LOOKUP_FILTER_PREFIX,
    LOOKUP_FILTER_WILDCARD,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
    LOOKUP_QUERY_EXCLUDE,
)
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    IdsFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
    SearchFilterBackend,
    CompoundSearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import BaseDocumentViewSet,DocumentViewSet
from django_elasticsearch_dsl_drf.pagination import PageNumberPagination

from search_indexes.documents.product import ProductDocument #CategoryDocument
from search_indexes.serializers.product import ProductDocumentSerializer




class ProductDocumentView(BaseDocumentViewSet):
    """The ProductDocument view."""

    document = ProductDocument
    serializer_class = ProductDocumentSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'
    filter_backends = [
        FilteringFilterBackend,
        IdsFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        CompoundSearchFilterBackend,
    ]
    # Define search fields
    search_fields = (
        'name',
        'description',
    )
    # Define filter fields
    filter_fields = {
                    'id': {
                                'field': 'id',
                                # Note, that we limit the lookups of id field in this example,
                                # to `range`, `in`, `gt`, `gte`, `lt` and `lte` filters.
                                'lookups': [
                                    LOOKUP_FILTER_RANGE,
                                    LOOKUP_QUERY_IN,
                                    LOOKUP_QUERY_GT,
                                    LOOKUP_QUERY_GTE,
                                    LOOKUP_QUERY_LT,
                                    LOOKUP_QUERY_LTE,
                                ],
                            },
                    'name': 'name.raw',
                    'category': 'category.raw',
                    'price': {
                                'field': 'price.raw',
                                # Note, that we limit the lookups of `price` field in this
                                # example, to `range`, `gt`, `gte`, `lt` and `lte` filters.
                                'lookups': [
                                    LOOKUP_FILTER_RANGE,
                                    LOOKUP_QUERY_GT,
                                    LOOKUP_QUERY_GTE,
                                    LOOKUP_QUERY_LT,
                                    LOOKUP_QUERY_LTE,
                                ],
                            },
                    'pages': {
                                'field': 'pages',
                                # Note, that we limit the lookups of `pages` field in this
                                # example, to `range`, `gt`, `gte`, `lt` and `lte` filters.
                                'lookups': [
                                    LOOKUP_FILTER_RANGE,
                                    LOOKUP_QUERY_GT,
                                    LOOKUP_QUERY_GTE,
                                    LOOKUP_QUERY_LT,
                                    LOOKUP_QUERY_LTE,
                                ],
                            },


                     }

    # Define ordering fields
    ordering_fields = {
        'id': 'id',
        'name': 'name.raw',
        'price': 'price.raw',

    }
    # Specify default ordering
    ordering = ('id', 'name', 'price',)


