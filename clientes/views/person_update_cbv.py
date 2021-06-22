'''
Favor colocar as importações em ordem alfabética para uma melhor organização
'''

from ..models import Person
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

class PersonUpdateView(UpdateView):
    model = Person
    fields = '__all__'
    template_name = 'clientes/person_update_form.html'
    success_url = reverse_lazy('person_list_cbv')