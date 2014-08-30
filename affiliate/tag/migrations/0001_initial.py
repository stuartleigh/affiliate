# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField(max_length=128)),
                ('description', models.TextField()),
                ('site', models.ForeignKey(to='site.Site')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
