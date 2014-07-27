# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20140727_1433'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set([(b'site', b'slug')]),
        ),
    ]
