# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 01:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default='aa', verbose_name='Data'),
            preserve_default=False,
        ),
    ]