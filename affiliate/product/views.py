import datetime

from django import http
from django.conf import settings
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

from affiliate.utils.shortcuts import redirect_back

from .models import Product


def product_detail(request, slug):

	try:
		product = Product.objects.select_related('currency', 'partner_site').get(site=request.site, slug=slug)
	except Product.DoesNotExist:
		raise http.Http404

	# saves an SQL lookup when rendering product.get_absolute_url
	product.site = request.site

	context = {
		'product': product,
		'tags': product.tags.all(),
		'similar_products': product.similar_products(count=4),
	}

	return render(request, "detail.html", context)


def product_api(request):
	try:
		page_num = int(request.GET['page'])
	except (ValueError, KeyError):
		return http.HttpResponseBadRequest()

	page_size = settings.PRODUCT_API_PAGE_SIZE
	offset = (page_num - 1) * page_size

	products = Product.objects.filter(site=request.site)[offset:offset+page_size]

	if not products:
		return http.HttpResponseBadRequest()

	return render(request, 'snippets/product_grid.html', {"products": products});


@permission_required('product.change_product')
def resurface_product(request, id):

	try:
		product = Product.objects.get(id=id)
	except Product.DoesNotExist:
		raise http.Http404

	product.added_date = datetime.datetime.now()
	product.save()

	return redirect_back(request)