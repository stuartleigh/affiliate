from django.contrib import admin

from .models import Product, Currency


admin.site.register(Product)
admin.site.register(Currency)