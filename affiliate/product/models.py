from random import shuffle

from django.core.urlresolvers import reverse
from django.db import models


def _get_standard_upload_folder(instance, filename):
	return u"{}/standard/{}".format(instance.site.domain, filename)

def _get_promo_upload_folder(instance, filename):
	return u"{}/promo/{}".format(instance.site.domain, filename)

class Product(models.Model):

	THEME_CHOICES = (
		('light', 'Light'),
		('dark', 'Dark'),
	)

	title = models.TextField()
	slug = models.SlugField(max_length=128, blank=True)

	external_url = models.URLField()
	product_ref = models.CharField(max_length=255, unique=True)

	description = models.TextField()
	price = models.DecimalField(decimal_places=2, max_digits=7)
	currency = models.ForeignKey('product.Currency')

	is_promo = models.BooleanField(default=False)
	partner_site = models.ForeignKey('site.AffiliateSite')
	site = models.ForeignKey('site.Site', related_name="products")

	added_date = models.DateTimeField(auto_now_add=True)

	image = models.ImageField(upload_to=_get_standard_upload_folder, blank=True, null=True)
	promo_image = models.ImageField(upload_to=_get_promo_upload_folder, blank=True, null=True)
	theme = models.CharField(max_length=15, choices=THEME_CHOICES, default='light')

	tags = models.ManyToManyField('tag.Tag', blank=True, null=True)

	class Meta:
		ordering = ['-added_date']
		unique_together = ("site", "slug")

	def __unicode__(self):
		return u"{}: {}".format(self.product_ref, self.title)

	def get_relative_url(self):
		return reverse('product-detail', kwargs={"slug": self.slug})

	def get_absolute_url(self):
		return u"http://{domain}{path}".format(domain=self.site.domain, path=self.get_relative_url())

	def similar_products(self, count=4):
		products = list(Product.objects.filter(site_id=self.site_id).exclude(id=self.id))
		shuffle(products)
		return products[:count]


class Currency(models.Model):
	iso_4217 = models.CharField(max_length=5)
	symbol = models.CharField(max_length=5)

	def __unicode__(self):
		return u"{}: {}".format(self.iso_4217, self.symbol)