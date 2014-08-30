from django.conf.urls import patterns, include, url
from django.contrib import admin

handler404 = 'affiliate.views.custom_404'
handler500 = 'affiliate.views.custom_500'

urlpatterns = patterns('',
    url(r'^$', 'affiliate.views.home', name='home'),
    url(r'^p/', include('affiliate.product.urls')),
    url(r'^t/', include('affiliate.tag.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitemap.xml$', 'affiliate.views.sitemap', name='sitemap'),
)
