from django.db import models


class Site(models.Model):
	name = models.CharField(max_length=255, unique=True)
	domain = models.CharField(max_length=255, db_index=True)

	meta_title = models.TextField(blank=True)
	meta_description = models.TextField(blank=True)

	story = models.TextField(blank=True)

	tracking_code = models.CharField(max_length=128, blank=True)

	def __unicode__(self):
		return unicode(self.name)


class AffiliateSite(models.Model):
	name = models.CharField(max_length=255)
	domain = models.CharField(max_length=255)
	affiliate_tracking_code = models.TextField()

	def __unicode__(self):
		return unicode(self.name)