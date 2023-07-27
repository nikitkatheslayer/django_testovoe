from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets

from controlcars.models import brand_car
from controlcars.serializers import BrandCarSerializer


@extend_schema_view(
    list=extend_schema(tags=['Марки']),
    retrieve=extend_schema(tags=['Марки']),
    create=extend_schema(tags=['Марки']),
    update=extend_schema(tags=['Марки']),
    partial_update=extend_schema(tags=['Марки']),
    destroy=extend_schema(tags=['Марки']),
)
class BrandCarViewSet(viewsets.ModelViewSet):
    queryset = brand_car.objects.all()
    serializer_class = BrandCarSerializer