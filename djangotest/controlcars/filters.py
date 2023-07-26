from django_filters import rest_framework as filters
from .models import orders

class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class OrdersFilter(filters.FilterSet):
    brand = filters.BaseInFilter(lookup_expr='in', field_name='model__brand')
    count = filters.OrderingFilter(fields={'count': 'count'})

    class Meta:
        model = orders
        fields = ['brand', 'count']