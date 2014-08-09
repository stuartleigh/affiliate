# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_theme'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='external_url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='product',
            name='external_path',
        ),
    ]
