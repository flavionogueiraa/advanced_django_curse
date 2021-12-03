'''
Shift + Alt + O para organizar as importações (vs code)
'''

from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

from ..models import Person


class PersonDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ['clientes.delete_person']

    model = Person
    success_url = reverse_lazy('person_list_cbv')
