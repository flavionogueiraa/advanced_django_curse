'''
Favor colocar as importações em ordem alfabética para uma melhor organização
'''

from ..models import Person
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy

def person_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    
    if request.method == 'POST':
        person.delete()
        return redirect(reverse_lazy(
            'person_list'
        ))

    context = {
        'person': person,
    }

    return render(
        request,
        'person_delete.html',
        context
    )