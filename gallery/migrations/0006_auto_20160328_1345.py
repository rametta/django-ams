# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_auto_20160328_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='image',
            field=models.ImageField(upload_to='work_images/%Y/%m/%d'),
        ),
    ]
