from django.shortcuts import render

from .models import Tag

# Create your views here.

def tagged_product_list(request, slug):

	try:
		tag = Tag.objects.get(site=request.site, slug=slug)
	except Tag.DoesNotExist:
		raise http.Http404

	context = {
		'tag': tag,
	}

	return render(request, "tagged_product_list.html", context)