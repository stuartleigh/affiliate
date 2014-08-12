import markdown as Markdown
import re

from django import template
from django.utils.safestring import mark_safe

 
register = template.Library()


SUMMARY_RE = re.compile("(.*?)(\\r\\n|\\n)")
 
@register.filter
def markdown(text):
	return mark_safe(Markdown.markdown(text, safe_mode='escape'))


@register.filter
def summary(text):
	match = SUMMARY_RE.match(text)
	try:
		return match.groups()[0]
	except AttributeError:
		return text