# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='domain',
            field=models.CharField(max_length=255, db_index=True),
        ),
    ]
