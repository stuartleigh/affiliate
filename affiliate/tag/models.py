from django.core.urlresolvers import reverse
from django.db import models


class Tag(models.Model):

	title = models.CharField(max_length=128)
	slug = models.SlugField(max_length=128)
	description = models.TextField()
	site = models.ForeignKey('site.Site')
	
	def __unicode__(self):
		return unicode(self.title)

	def get_absolute_url(self):
		return reverse('tagged-product-list', kwargs={"slug": self.slug})