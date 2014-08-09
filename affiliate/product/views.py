import datetime

from django import http
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

from affiliate.utils.shortcuts import redirect_back

from .models import Product


def product_detail(request, slug):

	try:
		product = Product.objects.select_related('currency').get(site=request.site, slug=slug)
	except Product.DoesNotExist:
		raise http.Http404

	context = {
		'product': product,
		'similar_products': product.similar_products(count=4),
	}

	return render(request, "detail.html", context)


@permission_required('product.change_product')
def resurface_product(request, id):

	try:
		product = Product.objects.get(id=id)
	except Product.DoesNotExist:
		raise http.Http404

	product.added_date = datetime.datetime.now()
	product.save()

	return redirect_back(request)