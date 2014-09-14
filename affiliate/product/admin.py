from django.contrib import admin
from django.core.urlresolvers import reverse

from affiliate.tag.models import Tag

from .models import Product, Currency


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_ref', 'title', 'added_date', 'is_promo', 'resurface')
    list_filter = ('is_promo', 'site__domain')

    prepopulated_fields = {"slug": ("title",)}

    filter_horizontal = ('tags',)

    def resurface(self, product):
            return "<a href='{}'>resurface</a>".format(reverse('product-resurface', kwargs={'id': product.id}))
    resurface.allow_tags = True

    def get_form(self, request, obj=None, **kwargs):
    	if obj:
    		self.obj = obj
    	return super(ProductAdmin, self).get_form(request, obj=obj, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
    	if hasattr(self, 'obj'):
    		site = self.obj.site
    	else:
    		site = request.site

        kwargs["queryset"] = Tag.objects.filter(site=site)
        return super(ProductAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)


admin.site.register(Currency)
