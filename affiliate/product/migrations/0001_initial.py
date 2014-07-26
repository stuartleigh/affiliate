# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import affiliate.product.models


class Migration(migrations.Migration):

    dependencies = [
        ('site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('iso_4217', models.CharField(max_length=5)),
                ('symbol', models.CharField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_ref', models.CharField(unique=True, max_length=255)),
                ('external_path', models.TextField()),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('price', models.DecimalField(max_digits=7, decimal_places=2)),
                ('is_active', models.BooleanField(default=True)),
                ('is_promo', models.BooleanField(default=False)),
                ('index', models.IntegerField(default=0)),
                ('image', models.ImageField(null=True, upload_to=affiliate.product.models._get_standard_upload_folder, blank=True)),
                ('promo_image', models.ImageField(null=True, upload_to=affiliate.product.models._get_promo_upload_folder, blank=True)),
                ('currency', models.ForeignKey(to='product.Currency')),
                ('partner_site', models.ForeignKey(to='site.AffiliateSite')),
                ('site', models.ForeignKey(to='site.Site')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
