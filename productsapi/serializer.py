from rest_framework import serializers

from products.models import Product, Category



class ProductSerializer(serializers.ModelSerializer):
    # category = CategorySerializer(read_only=True, many=True)

    class Meta:
        model = Product
        # fields = '__all__'
        fields = (
            "category",
            "id",
            "name",
            "price",
            "quantity",
            "description",
            "picture",
            "slug",
        )
        lookup_field = "slug"

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=True, many=True)
    class Meta:
        model = Category
        fields = ("id", "name","products",)
        #fields = '__all__'







