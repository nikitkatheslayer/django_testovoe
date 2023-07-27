from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets

from controlcars.models import color_car
from controlcars.serializers import ColorCarSerializer


@extend_schema_view(
    list=extend_schema(tags=['Цвета автомобилей']),
    retrieve=extend_schema(tags=['Цвета автомобилей']),
    create=extend_schema(tags=['Цвета автомобилей']),
    update=extend_schema(tags=['Цвета автомобилей']),
    partial_update=extend_schema(tags=['Цвета автомобилей']),
    destroy=extend_schema(tags=['Цвета автомобилей']),
)
class ColorCarViewSet(viewsets.ModelViewSet):
    queryset = color_car.objects.all()
    serializer_class = ColorCarSerializer