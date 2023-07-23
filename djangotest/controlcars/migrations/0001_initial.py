# Generated by Django 4.2.3 on 2023-07-22 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='brand_car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Наименование бренда')),
                ('country', models.CharField(max_length=128, verbose_name='Страна')),
                ('logo', models.ImageField(upload_to='brand_logo', verbose_name='Логотип бренда')),
            ],
        ),
        migrations.CreateModel(
            name='color_car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название цвета')),
                ('code', models.PositiveIntegerField(verbose_name='Код цвета')),
                ('hex_code', models.CharField(max_length=10, verbose_name='HEX-код цвета')),
            ],
        ),
        migrations.CreateModel(
            name='model_car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Наименование марки')),
                ('year', models.PositiveSmallIntegerField(verbose_name='Год')),
                ('price', models.PositiveIntegerField(verbose_name='Стоимость')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controlcars.brand_car', verbose_name='Бренд')),
            ],
        ),
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(verbose_name='Количество')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controlcars.color_car', verbose_name='Цвет автомобиля')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controlcars.model_car', verbose_name='Модель автомобиля')),
            ],
        ),
    ]
