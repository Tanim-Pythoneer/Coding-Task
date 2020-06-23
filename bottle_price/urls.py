from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('bottle_price', views.PriceListView)

urlpatterns = [
    path('', include(router.urls)),
    path('/calculate', views.PriceListView.calculate)

]
