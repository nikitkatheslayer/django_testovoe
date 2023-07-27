from django.db.models import Sum
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from controlcars.models import model_car
from controlcars.serializers import SumCarsSerializer


@extend_schema(
    tags=['Сумма по маркам']
)
class SumCarsModelAPIView(ListAPIView):
    queryset = model_car.objects.annotate(sum_cars=Sum('orders__count'))
    serializer_class = SumCarsSerializer
    permission_classes = [IsAuthenticated, ]

