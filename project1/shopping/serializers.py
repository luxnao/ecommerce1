from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('slug','name','small_description','quantity','original_price','selling_price')
