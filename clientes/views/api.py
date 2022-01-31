#Shift + Alt + O para organizar as importações (vs code)

from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.http.response import JsonResponse
from produtos.models import Produto


@login_required
def api(request):
    cliente = {
        'nome': 'Flavio',
        'idade': '30',
        'salario': 1000.00
    }
    lista = [1, 2, 3, 4, 5]
    produto = Produto.objects.last()
    lista_produto = [model_to_dict(produto) for produto in Produto.objects.all()]

    return JsonResponse(lista_produto, safe=False)
