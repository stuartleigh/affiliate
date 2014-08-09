from django import http
from django.core.urlresolvers import reverse


def redirect_back(request):
    """ Redirects to the previous page if reff - otherwise home """
    return http.HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('home')))