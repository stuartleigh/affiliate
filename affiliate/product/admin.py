from django.contrib import admin

from .models import Product, Currency


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_ref', 'title', 'index', 'is_active', 'is_promo')
    list_editable = ('index',)
    list_filter = ('is_active', 'is_promo', 'site__domain')


admin.site.register(Currency)