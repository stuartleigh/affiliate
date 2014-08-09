from django.shortcuts import render


def home(request):
	products = request.site.products.select_related('currency')
	promos = products.filter(is_promo=True)

	context = {
		"products": products,
		"promos": promos,
	}

	return render(request, "home.html", context)