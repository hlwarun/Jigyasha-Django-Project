# Generated by Django 3.0.8 on 2020-08-04 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='large_text',
        ),
        migrations.AddField(
            model_name='banner',
            name='large_text1',
            field=models.CharField(default='Summer', max_length=15),
        ),
        migrations.AddField(
            model_name='banner',
            name='large_text2',
            field=models.CharField(default='Collection', max_length=15),
        ),
    ]
