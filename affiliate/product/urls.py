from django.conf.urls import patterns, include, url

urlpatterns = patterns('affiliate.product.views',
	url(r'^(?P<slug>[a-z0-9-]+)/$', 'product_detail', name='product-detail'),
)