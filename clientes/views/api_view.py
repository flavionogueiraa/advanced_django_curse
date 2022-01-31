#Shift + Alt + O para organizar as importações (vs code)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views.generic.base import View
from produtos.models import Produto


class ApiView(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'nome': 'Flavio',
            'idade': '30',
            'salario': 1000.00
        }
        lista_produto = [model_to_dict(produto) for produto in Produto.objects.all()]

        return JsonResponse(lista_produto, safe=False)
