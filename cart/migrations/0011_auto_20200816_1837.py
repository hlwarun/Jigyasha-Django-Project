# Generated by Django 3.0.8 on 2020-08-16 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0010_auto_20200816_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='single_total',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
