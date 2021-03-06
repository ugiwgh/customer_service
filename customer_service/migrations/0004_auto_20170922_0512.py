# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-22 05:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer_service', '0003_menu_rolebindmenu'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rolebindmenu',
            options={'verbose_name': '功能权限绑定', 'verbose_name_plural': '功能权限绑定'},
        ),
        migrations.AddField(
            model_name='game',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='rolebindmenu',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_service.Role', verbose_name='角色'),
        ),
    ]
