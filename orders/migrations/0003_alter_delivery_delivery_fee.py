# Generated by Django 4.1.7 on 2023-08-22 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_delivery_delivery_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='delivery_fee',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
