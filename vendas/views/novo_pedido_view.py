'''
Shift + Alt + O para organizar as importações (vs code)
'''

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.base import View


class NovoPedidoView(LoginRequiredMixin, View):
    def get(self, request):
        return render(
            request,
            'vendas/novo_pedido.html'
        )

    def post(self, request):
        return render(
            request,
            'vendas/novo_pedido.html'
        )