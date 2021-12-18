'''
Shift + Alt + O para organizar as importações (vs code)
'''

from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse


@login_required
def api(request):
    cliente = {
        'nome': 'Flavio',
        'idade': '30',
        'salario': 1000.00
    }

    lista = [1, 2, 3, 4, 5]

    return JsonResponse(lista, safe=False)
