'''
Shift + Alt + O para organizar as importações (vs code)
'''

from ..models import Person
from django.views.generic.list import ListView

class PersonList(ListView):
    model = Person