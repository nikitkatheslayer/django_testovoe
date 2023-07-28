from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from controlcars.models import model_car
from controlcars.serializers.serializers import ModelCarSerializer


@extend_schema_view(
    list=extend_schema(tags=['Модели']),
    retrieve=extend_schema(tags=['Модели']),
    create=extend_schema(tags=['Модели']),
    update=extend_schema(tags=['Модели']),
    partial_update=extend_schema(tags=['Модели']),
    destroy=extend_schema(tags=['Модели']),
)
class ModelCarViewSet(viewsets.ModelViewSet):
    queryset = model_car.objects.all()
    serializer_class = ModelCarSerializer
    permission_classes = [IsAuthenticated, ]