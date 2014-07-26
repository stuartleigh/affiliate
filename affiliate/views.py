from django.shortcuts import render


def home(request):
	products = request.site.products.select_related('currency').filter(is_active=True)
	promos = products.filter(is_promo=True)

	context = {
		"site": request.site,
		"products": products,
		"promos": promos,
	}

	return render(request, "home.html", context)