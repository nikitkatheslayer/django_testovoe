from django.db import models
from django.utils import timezone
from django.utils.datetime_safe import date, datetime

class color_car(models.Model):
    name = models.CharField(max_length=64,
                            verbose_name='Название цвета')
    code = models.PositiveIntegerField(verbose_name="Код цвета")
    hex_code = models.CharField(max_length=10,
                                verbose_name='HEX-код цвета')

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return f'{self.name} - {self.code}'

class brand_car(models.Model):
    name = models.CharField(max_length=128,
                            verbose_name='Наименование бренда')
    country = models.CharField(max_length=128,
                               verbose_name='Страна')
    logo = models.ImageField(upload_to='brand_logo',
                             verbose_name='Логотип бренда')

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name



class model_car(models.Model):
    name = models.CharField(max_length=128,
                            verbose_name='Наименование марки')
    year = models.PositiveSmallIntegerField(verbose_name='Год')
    price = models.PositiveIntegerField(verbose_name="Стоимость")
    brand = models.ForeignKey(brand_car,
                              verbose_name='Бренд',
                              on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'

    def __str__(self):
        return self.name

class orders(models.Model):
    color = models.ForeignKey(color_car,
                              verbose_name='Цвет автомобиля',
                              on_delete=models.CASCADE)
    model = models.ForeignKey(model_car,
                              verbose_name='Модель автомобиля',
                              on_delete=models.CASCADE)
    count = models.PositiveIntegerField(verbose_name="Количество")
    date = models.DateField(verbose_name='Дата',
                            blank=True,
                            null=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


    def __str__(self):
        return f'Заказ №{format(self.id)}'
