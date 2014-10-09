from django.conf.urls import patterns, include, url

urlpatterns = patterns('affiliate.product.views',
	url(r'^api/$', 'product_api', name="product-api"),
	url(r'^(?P<slug>[a-z0-9-]+)/$', 'product_detail', name='product-detail'),
	url(r'^(?P<id>[0-9]+)/resurface/$', 'resurface_product', name='product-resurface'),
)