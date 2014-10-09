import random

from django.core.files.storage import FileSystemStorage


class KittenStorage(FileSystemStorage):
	def url(self, name):
		if "promo" in name:
			val = 1200
		else:
			val = 400
		val = val + random.randrange(1, 100) + len(name)
		return "http://lorempixel.com/{0}/{0}".format(val)