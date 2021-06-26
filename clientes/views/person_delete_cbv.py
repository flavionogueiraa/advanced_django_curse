'''
Favor colocar as importações em ordem alfabética para uma melhor organização
'''

from ..models import Person
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

class PersonDeleteView(DeleteView):
    model = Person
    success_url = reverse_lazy('person_list_cbv')