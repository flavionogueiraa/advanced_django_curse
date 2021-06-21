'''
Favor colocar as importações em ordem alfabética para uma melhor organização
'''

from ..forms import PersonForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

@login_required
def person_form(request):
    if request.method == 'POST':
        form = PersonForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            form.save()
            return redirect(reverse_lazy(
                'person_list_cbv'
            ))
    else:
        form = PersonForm(None)

    context = {
        'form': form,
    }

    return render(
        request,
        'person_form.html',
        context
    )