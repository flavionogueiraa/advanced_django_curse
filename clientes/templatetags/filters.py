'''
Favor colocar as importações em ordem alfabética para uma melhor organização
'''

from django import template

register = template.Library()

@register.filter
def my_first_filter(data):
    return '{} - Meu primeiro filtro'.format(data)