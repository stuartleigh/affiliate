from django import http

from ..models import Site


class MultiSiteMiddleware(object):
	
	def process_request(self, request):
		try:
			domain = request.get_host().split(":")[0]
			request.site = Site.objects.get(domain=domain)
		except Site.DoesNotExist:
			return http.HttpResponseNotFound()
