from django.contrib import admin
from django.core.urlresolvers import reverse

from .models import Product, Currency


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_ref', 'title', 'added_date', 'is_promo', 'resurface')
    list_filter = ('is_promo', 'site__domain')

    prepopulated_fields = {"slug": ("title",)}

    def resurface(self, product):
            return "<a href='{}'>resurface</a>".format(reverse('product-resurface', kwargs={'id': product.id}))
    resurface.allow_tags = True


admin.site.register(Currency)