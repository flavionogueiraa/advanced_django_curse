'''
Favor colocar as importações em ordem alfabética para uma melhor organização
'''

from ..models import Person
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def person_list(request):
    persons = Person.objects.all()

    context = {
        'persons': persons,
    }

    return render(
        request,
        'person_list.html',
        context
    )