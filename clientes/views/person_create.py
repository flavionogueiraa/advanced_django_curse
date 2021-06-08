'''
Favor colocar as importações em ordem alfabética para uma melhor organização
'''

from ..forms import PersonForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

def person_create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect(reverse_lazy(
                'persons_list'
            ))
    else:
        form = PersonForm(None)

    context = {
        'form': form,
    }

    return render(
        request,
        'person_create.html',
        context
    )