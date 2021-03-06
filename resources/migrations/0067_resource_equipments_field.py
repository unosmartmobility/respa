# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-08 10:29
from __future__ import unicode_literals

from django.db import migrations
import resources.fields


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0066_support_for_django_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='equipment',
            field=resources.fields.EquipmentField(
                through='resources.ResourceEquipment',
                to='resources.Equipment',
                verbose_name='Equipment',
            ),
        ),
    ]
