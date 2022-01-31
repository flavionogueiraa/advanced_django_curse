#Shift + Alt + O para organizar as importações (vs code)

from decimal import Decimal

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import View

from ..forms import ItemVendaForm
from ..models import Venda


class NovoPedidoView(LoginRequiredMixin, View):
    def get(self, request):
        return render(
            request,
            'vendas/novo_pedido.html'
        )

    def post(self, request, id_venda):
        context = {}
        context['numero_venda'] = request.POST.get('numero_venda', None)
        context['desconto'] = request.POST.get('desconto', None)
        context['venda_id'] = request.POST.get('venda_id', None)

        if context['venda_id']:
            context['venda'] = get_object_or_404(Venda, pk=context['venda_id'])
        else:
            context['venda'] = Venda.objects.create(
                numero_venda=context['numero_venda'],
                desconto=Decimal(context['desconto'])
            )
        context['venda_id'] = context['venda'].id

        
        return render(
            request,
            'vendas/novo_pedido.html',
            context
        )
