'''
Shift + Alt + O para organizar as importações (vs code)
'''

from .models import Person
from django.forms import ModelForm, fields

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'