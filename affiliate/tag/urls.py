from django.conf.urls import patterns, include, url

urlpatterns = patterns('affiliate.tag.views',
	url(r'^(?P<slug>[a-z0-9-]+)/$', 'tagged_product_list', name='tagged-product-list'),
)