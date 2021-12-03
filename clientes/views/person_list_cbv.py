'''
Shift + Alt + O para organizar as importações (vs code)
'''

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from ..models import Person


class PersonList(LoginRequiredMixin, ListView):
    model = Person
