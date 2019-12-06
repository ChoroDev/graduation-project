# Generated by Django 3.0 on 2019-12-06 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('automated_system', '0002_auto_20191206_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='maintainer',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='automated_system.Staff'),
        ),
        migrations.AddField(
            model_name='staff',
            name='group',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.Group'),
        ),
    ]
