'''
Favor colocar as importações em ordem alfabética para uma melhor organização
'''

from ..models import Person
from django.views.generic.detail import DetailView

class PersonDetailView(DetailView):
    model = Person