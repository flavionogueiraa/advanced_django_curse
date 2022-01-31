#Shift + Alt + O para organizar as importações (vs code)

from datetime import datetime
from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def current_time(context, format_string):
    return datetime.now().strftime(format_string)