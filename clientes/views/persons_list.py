'''
Favor colocar as importações em ordem alfabética para uma melhor organização
'''

from ..models import Person
from django.shortcuts import render

def persons_list(request):
    persons = Person.objects.all()

    context = {
        'persons': persons,
    }

    return render(
        request,
        'pessoa.html',
        context
    )