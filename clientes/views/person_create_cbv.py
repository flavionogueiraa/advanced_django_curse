#Shift + Alt + O para organizar as importações (vs code)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from ..models import Person


class PersonCreateView(LoginRequiredMixin, CreateView):
    model = Person
    fields = '__all__'
    success_url = reverse_lazy('person_list_cbv')
