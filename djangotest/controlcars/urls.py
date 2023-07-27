from django.urls import path

from rest_framework.routers import DefaultRouter
from controlcars.views.sumcolor_viewset import SumCarsColorAPIView
from controlcars.views.summodel_viewset import SumCarsModelAPIView
from controlcars.views.brandcar_viewset import BrandCarViewSet
from controlcars.views.colorcar_viewset import ColorCarViewSet
from controlcars.views.modelcar_viewset import ModelCarViewSet
from controlcars.views.orders_viewset import OrdersViewSet

app_name = 'api'

router = DefaultRouter()
router.register('color_car', ColorCarViewSet, basename='color_car')
router.register('brand', BrandCarViewSet, basename='brand')
router.register('model', ModelCarViewSet, basename='model')
router.register('orders', OrdersViewSet, basename='orders')

urlpatterns = [
    path('sum_cars/brand/', SumCarsModelAPIView.as_view()),
    path('sum_cars/color/', SumCarsColorAPIView.as_view()),
]

urlpatterns += router.urls
