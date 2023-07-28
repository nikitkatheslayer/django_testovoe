from django.db.models import Sum
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from controlcars.models import color_car
from controlcars.serializers.serializers import CountCarsSerializer


@extend_schema(
    tags=['Сумма по цветам']
)
class SumCarsColorAPIView(ListAPIView):
    queryset = color_car.objects.annotate(sum_cars=Sum('orders__count'))
    serializer_class = CountCarsSerializer
    permission_classes = [IsAuthenticated, ]