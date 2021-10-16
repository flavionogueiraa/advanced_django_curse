'''
Shift + Alt + O para organizar as importações (vs code)
'''

from ..models import Person
from django.views.generic.detail import DetailView

class PersonDetailView(DetailView):
    model = Person