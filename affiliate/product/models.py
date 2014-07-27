from django.db import models


def _get_standard_upload_folder(instance, filename):
	return u"{}/standard/{}".format(instance.site.domain, filename)

def _get_promo_upload_folder(instance, filename):
	return u"{}/promo/{}".format(instance.site.domain, filename)

class Product(models.Model):
	product_ref = models.CharField(max_length=255, unique=True)
	external_path = models.TextField()
	title = models.TextField()
	description = models.TextField()
	price = models.DecimalField(decimal_places=2, max_digits=7)
	currency = models.ForeignKey('product.Currency')
	is_active = models.BooleanField(default=True)
	is_promo = models.BooleanField(default=False)
	partner_site = models.ForeignKey('site.AffiliateSite')
	site = models.ForeignKey('site.Site', related_name="products")
	index = models.IntegerField(default=0)

	image = models.ImageField(upload_to=_get_standard_upload_folder, blank=True, null=True)
	promo_image = models.ImageField(upload_to=_get_promo_upload_folder, blank=True, null=True)

	class Meta:
		ordering = ['-index']

	def __unicode__(self):
		return u"{}: {}".format(self.product_ref, self.title)

	def url(self):
		site = self.partner_site
		return u"{domain}{path}{code}".format(
			domain=site.domain,
			path=self.external_path,
			code=site.affiliate_tracking_code
		)


class Currency(models.Model):
	iso_4217 = models.CharField(max_length=5)
	symbol = models.CharField(max_length=5)

	def __unicode__(self):
		return u"{}: {}".format(self.iso_4217, self.symbol)