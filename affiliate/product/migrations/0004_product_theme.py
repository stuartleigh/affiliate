# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20140727_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='theme',
            field=models.CharField(default=b'light', max_length=15, choices=[(b'light', b'Light'), (b'dark', b'Dark')]),
            preserve_default=True,
        ),
    ]
