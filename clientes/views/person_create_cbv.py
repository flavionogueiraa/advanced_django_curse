'''
Favor colocar as importações em ordem alfabética para uma melhor organização
'''

from ..models import Person
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

class PersonCreateView(CreateView):
    model = Person
    fields = '__all__'
    success_url = reverse_lazy('person_list_cbv')