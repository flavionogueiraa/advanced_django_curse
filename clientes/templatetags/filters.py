#Shift + Alt + O para organizar as importações (vs code)

from django import template

register = template.Library()

@register.filter
def my_first_filter(data):
    return '{} - Meu primeiro filtro'.format(data)