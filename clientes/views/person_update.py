'''
Favor colocar as importações em ordem alfabética para uma melhor organização
'''

from ..forms import PersonForm
from ..models import Person
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy

def person_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect(reverse_lazy(
            'person_list'
        ))

    context = {
        'form': form,
    }

    return render(
        request,
        'person_form.html',
        context
    )