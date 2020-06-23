from django.shortcuts import render
from rest_framework import viewsets
from .models import pricelist
from .serializers import PriceListSerializer

class PriceListView(viewsets.ModelViewSet):
    queryset = pricelist.objects.all()
    serializer_class = PriceListSerializer

    def calculate(self, request):
        if self.request.method == 'GET':
            num = self.request.GET.get('number', None)
        priceUnitBottle = 1
        priceUnitPack = 5
        priceUnitBox = 10

        if num >= 11:
            numPacks = num // 11
            numBoxs = numPacks // 24
            if numBoxs < 1:
                remainingBottles = num - (numPacks * 11)
                price = numPacks * priceUnitPack + remainingBottles * priceUnitBottle
            else:
                remainingPacks = numPacks % 24
                remainingBottles = num - (numBoxs * 24 * 11) - (remainingPacks * 11)
                price = numBoxs * priceUnitBox + numPacks * priceUnitPack + remainingBottles * priceUnitBottle
        else:
            price = num * priceUnitBottle
        return render(request,'bottle_price/index.html', {result: price})

    