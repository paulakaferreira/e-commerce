# Generated by Django 4.1.7 on 2023-08-23 17:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_orderproduct_price_alter_delivery_delivery_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='delivery_date',
            field=models.DateField(default=datetime.datetime(2023, 8, 25, 17, 16, 53, 928927)),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='estimated_arrival_date',
            field=models.DateField(default=datetime.datetime(2023, 8, 28, 17, 16, 53, 928914)),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
