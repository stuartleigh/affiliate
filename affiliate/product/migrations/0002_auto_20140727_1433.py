# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': [b'-index']},
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='', max_length=128, blank=True),
            preserve_default=False,
        ),
    ]
