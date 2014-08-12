import random

from django.shortcuts import render


def home(request):
	products = request.site.products.select_related('currency')
	promos = products.filter(is_promo=True)

	context = {
		"products": products,
		"promos": promos,
	}

	return render(request, "home.html", context)


def sitemap(request):
	products = request.site.products.all()
	context = {"products": products}
	return render(request, "sitemap.xml", context, content_type="application/xhtml+xml")


def custom_404(request):
	count = request.site.products.count()
	random_num = random.choice(range(1, count))
	random_product = request.site.products.all()[random_num - 1]
	return render(request, '404.html', {"product": random_product})


def custom_500(request):
	count = request.site.products.count()
	random_num = random.choice(range(1, count))
	return render(request, '500.html')