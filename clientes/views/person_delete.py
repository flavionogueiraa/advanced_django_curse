#Shift + Alt + O para organizar as importações (vs code)

from ..models import Person
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy

@login_required
def person_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    
    if request.method == 'POST':
        person.delete()
        return redirect(reverse_lazy('person_list_cbv'))

    context = {
        'person': person,
    }

    return render(
        request,
        'person_delete.html',
        context
    )