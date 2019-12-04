# Generated by Django 2.2.3 on 2019-08-29 08:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_text',
        ),
        migrations.AddField(
            model_name='student',
            name='entry_date',
            field=models.DateField(default=datetime.datetime.today, verbose_name='Дата поступления'),
        ),
        migrations.AddField(
            model_name='student',
            name='faculty',
            field=models.CharField(default='None', max_length=255, verbose_name='Факультет'),
        ),
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.IntegerField(default=0, verbose_name='Номер группы'),
        ),
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(default='John', max_length=255, verbose_name='Имя студента'),
        ),
        migrations.AddField(
            model_name='student',
            name='specialty',
            field=models.CharField(default='None', max_length=255, verbose_name='Специальность'),
        ),
        migrations.AddField(
            model_name='student',
            name='surname',
            field=models.CharField(default='Doe', max_length=255, verbose_name='Фамилия студента'),
        ),
        migrations.DeleteModel(
            name='UserRiddle',
        ),
    ]