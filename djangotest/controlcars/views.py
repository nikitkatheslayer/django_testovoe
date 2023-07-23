from django.db.models import Sum, Count
from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from .models import color_car, brand_car, model_car, orders
from .serializers import ColorCarSerializer, BrandCarSerializer, ModelCarSerializer, OrdersSerializer, \
    SumCarsSerializer, CountCarsSerializer


class ColorCarViewSet(viewsets.ModelViewSet):
    queryset = color_car.objects.all()
    serializer_class = ColorCarSerializer

class BrandCarViewSet(viewsets.ModelViewSet):
    queryset = brand_car.objects.all()
    serializer_class = BrandCarSerializer

class ModelCarViewSet(viewsets.ModelViewSet):
    queryset = model_car.objects.all()
    serializer_class = ModelCarSerializer

class OrdersViewSet(viewsets.ModelViewSet):
    queryset = orders.objects.all()
    serializer_class = OrdersSerializer

class SumCarsAPIView(ListAPIView):
    queryset = model_car.objects.annotate(sum_cars=Sum('orders__count'))
    serializer_class = SumCarsSerializer

class CountCarAPIView(ListAPIView):
    queryset = color_car.objects.annotate(sum_cars=Sum('orders__model'))
    serializer_class = CountCarsSerializer