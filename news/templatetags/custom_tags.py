from datetime import datetime
from django import template

register = template.Library()


@register.simple_tag()
def current_time(format_string='%Y-%m-%d'):
    return datetime.now().strftime(format_string)

@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    d = context['request'].GET.copy()
    for key, value in kwargs.items():
        d[key] = value
    return d.urlencode()

