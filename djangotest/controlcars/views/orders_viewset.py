from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from controlcars.filters import OrdersFilter
from controlcars.models import orders
from controlcars.serializers import OrdersSerializer


@extend_schema_view(
    list=extend_schema(tags=['Заказы']),
    retrieve=extend_schema(tags=['Заказы']),
    create=extend_schema(tags=['Заказы']),
    update=extend_schema(tags=['Заказы']),
    partial_update=extend_schema(tags=['Заказы']),
    destroy=extend_schema(tags=['Заказы']),
)
class OrdersViewSet(viewsets.ModelViewSet):
    queryset = orders.objects.all()
    serializer_class = OrdersSerializer
    filterset_class = OrdersFilter
    permission_classes = [IsAuthenticated, ]