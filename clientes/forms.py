'''
Favor colocar as importações em ordem alfabética para uma melhor organização
'''

from .models import Person
from django.forms import ModelForm, fields

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'