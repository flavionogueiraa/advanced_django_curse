'''
Favor colocar as importações em ordem alfabética para uma melhor organização
'''

from datetime import datetime
from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def current_time(context, format_string):
    return datetime.now().strftime(format_string)