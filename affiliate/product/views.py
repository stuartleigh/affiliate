from django import http
from django.shortcuts import render

from .models import Product


def product_detail(request, slug):

	try:
		product = Product.objects.select_related('currency').get(site=request.site, slug=slug)
	except Product.DoesNotExist:
		raise http.Http404

	context = {
		'product': product,
		'site': request.site,
	}

	return render(request, "detail.html", context)