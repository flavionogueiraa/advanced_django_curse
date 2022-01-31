#Shift + Alt + O para organizar as importações (vs code)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from ..models import Person


class PersonUpdateView(LoginRequiredMixin, UpdateView):
    model = Person
    fields = '__all__'
    template_name = 'clientes/person_update_form.html'
    success_url = reverse_lazy('person_list_cbv')
