# Generated by Django 3.0.5 on 2020-05-25 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automated_system', '0012_auto_20200524_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='shelf_life',
            field=models.IntegerField(default=0),
        ),
    ]
