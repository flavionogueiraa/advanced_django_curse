'''
Favor colocar as importações em ordem alfabética para uma melhor organização
'''

from ..models import Person
from django.views.generic.list import ListView

class PersonList(ListView):
    model = Person