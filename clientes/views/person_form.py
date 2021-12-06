'''
Shift + Alt + O para organizar as importações (vs code)
'''

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from ..forms import PersonForm


@login_required
def person_form(request):
    if not request.user.has_perm('clientes.add_cliente'):
        raise PermissionDenied()
    
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
        'clientes/person_form.html',
        context
    )
