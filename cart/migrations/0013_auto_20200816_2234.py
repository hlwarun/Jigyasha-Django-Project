# Generated by Django 3.0.8 on 2020-08-16 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0012_auto_20200816_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='shipping_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='cart',
            name='tax_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='cart',
            name='subtotal_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
