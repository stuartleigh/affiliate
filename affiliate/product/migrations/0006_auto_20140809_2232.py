# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20140809_2137'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': [b'-added_date']},
        ),
        migrations.AddField(
            model_name='product',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 8, 9, 22, 32, 9, 48237), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='product',
            name='index',
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_active',
        ),
    ]
