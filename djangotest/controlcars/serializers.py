from django.utils.datetime_safe import date, datetime
from rest_framework import serializers
from .models import color_car, brand_car, model_car, orders

class ColorCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = color_car
        fields = '__all__'

class BrandCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = brand_car
        fields = '__all__'

class ModelCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = model_car
        fields = '__all__'

class ModelCarToOrderSerializer(serializers.ModelSerializer):
    brand = serializers.SlugRelatedField(read_only=True, slug_field='name')
    class Meta:
        model = model_car
        fields = ['name', 'brand']

class OrdersSerializer(serializers.ModelSerializer):
    model = ModelCarToOrderSerializer()
    class Meta:
        model = orders
        fields = '__all__'

class SumCarsSerializer(serializers.Serializer):
    brand_id = serializers.IntegerField()
    sum_cars = serializers.IntegerField()

class CountCarsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    sum_cars = serializers.IntegerField()
