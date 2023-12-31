# Generated by Django 4.2.3 on 2023-07-23 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlcars', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand_car',
            options={'verbose_name': 'Бренд', 'verbose_name_plural': 'Бренды'},
        ),
        migrations.AlterModelOptions(
            name='color_car',
            options={'verbose_name': 'Цвет', 'verbose_name_plural': 'Цвета'},
        ),
        migrations.AlterModelOptions(
            name='model_car',
            options={'verbose_name': 'Модель', 'verbose_name_plural': 'Модели'},
        ),
        migrations.AlterModelOptions(
            name='orders',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateField(blank=True, verbose_name='Дата'),
        ),
    ]
