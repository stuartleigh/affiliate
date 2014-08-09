import markdown as Markdown

from django import template
from django.utils.safestring import mark_safe

 
register = template.Library()

 
@register.filter
def markdown(text):
	return mark_safe(Markdown.markdown(text, safe_mode='escape'))