# Generated by Django 3.0.8 on 2020-08-18 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Ordered', 'Ordered'), ('Shipped', 'Shipped'), ('Abandoned', 'Abandoned'), ('Delivered', 'Delivered')], default='Ordered', max_length=12),
        ),
    ]
