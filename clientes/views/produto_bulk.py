'''
Shift + Alt + O para organizar as importações (vs code)
'''

from django.http.response import HttpResponse
from django.views.generic import View
from produtos.models import Produto


class ProdutoBulk(View):
    def get(self, request):
        produtos = [
            'Uva', 'Banana', 'Pera', 'Maçã',
            'Melancia', 'Melão', 'Carambola', 'Manga'
        ]
        lista_produtos = []

        for produto in produtos:
            instancia_produto = Produto(
                descricao=produto,
                preco=10.0
            )
            lista_produtos.append(instancia_produto)
        
        Produto.objects.bulk_create(lista_produtos)

        return HttpResponse('Funcionou')
