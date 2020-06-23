from rest_framework import serializers
from . models import pricelist

class PriceListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = pricelist
        fields = ('id', 'url', 'name', 'quantity', 'price')