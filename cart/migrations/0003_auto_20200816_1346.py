# Generated by Django 3.0.8 on 2020-08-16 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
        ('cart', '0002_auto_20200814_2236'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('added_at', models.DateTimeField(auto_now=True)),
                ('product', models.ManyToManyField(to='shop.Product')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(blank=True, null=True, to='cart.cartItem'),
        ),
    ]
