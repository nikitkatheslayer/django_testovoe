from django.forms import forms
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
    class Meta:
        model = model_car
        fields = ['name', 'brand']

class OrdersSerializer(serializers.ModelSerializer):
    model = ModelCarToOrderSerializer()
    class Meta:
        model = orders
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        model = validated_data.pop('model')
        current_model, status = model_car.objects.get_or_create(**model)
        print(current_model)
        print(status)
        order = orders.objects.create(model=current_model, **validated_data)

        return order

    def validate_date(self, attrs):
        if attrs is None:
            attrs = date.today()
        return attrs

    def validate_model(self, attrs):
        check_model = model_car.objects.filter(name=f"{attrs['name']}").exists()
        if not check_model:
            raise forms.ValidationError("Такая модель отсутствует в каталоге")
        return attrs

class SumCarsSerializer(serializers.Serializer):
    brand_id = serializers.IntegerField()
    sum_cars = serializers.IntegerField()

class CountCarsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    sum_cars = serializers.IntegerField()
