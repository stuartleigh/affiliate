# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20140809_2232'),
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to=b'tag.Tag', null=True, blank=True),
            preserve_default=True,
        ),
    ]
