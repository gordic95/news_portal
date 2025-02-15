from django import template

register = template.Library()
@register.filter
def censore(value):
    list_bad_words = ['Пенис', 'дурак', 'недоумок']
    if value in list_bad_words:
        return f'**{value[2:]}'
    else:
        return value
