'''
Favor colocar as importações em ordem alfabética para uma melhor organização
'''

from ..models import Person
from datetime import date
from django.views.generic.detail import DetailView

class PersonDetailView(DetailView):
    model = Person

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['today'] = date.today()
        return context