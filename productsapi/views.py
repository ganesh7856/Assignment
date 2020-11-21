from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.views import APIView

from django.views.generic import ListView

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from productsapi.serializer import ProductSerializer, CategorySerializer
from products.models import Product, Category


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    search_fields=('name',)
    ordering_fields = ('name',)
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "slug"
    search_fields = ('name','slug','price')
    ordering_fields = ('name','slug','price')
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]


# class ProductsDetailView(APIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#     def get(self, request, *args, **kwargs):
#             object = self.get_object()
#             object.count = int(object.count) + 1
#             object.save()
#             return super(ProductsDetailView, self).get(self, request, *args, **kwargs)

class CategoryDetailView(viewsets.ModelViewSet):
    queryset = Category.objects.order_by('name')
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]


    def list(self, request, *args, **kwargs):

        queryset = self.filter_queryset(self.get_queryset())
        for obj in queryset:
            obj.view_count = int(obj.view_count) + 1
            obj.save(update_fields=("view_count", ))
        return super().list(request, *args, **kwargs)