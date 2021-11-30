'''
Shift + Alt + O para organizar as importações (vs code)
'''

from django.db.models import Avg, Max, Min
from django.shortcuts import render
from django.views import View

from ..models import Venda


class DashboardView(View):
    def get(self, request):
        media_valor = Venda.objects.media()
        media_desconto = Venda.objects.media_desconto()
        menor_valor_venda = Venda.objects.menor_valor_venda()
        maior_valor_venda = Venda.objects.maior_valor_venda()
        quantidade_total_vendas = Venda.objects.quantidade_total_vendas()
        quantidade_total_vendas_com_nota_fiscal_emitida = Venda.objects.quantidade_total_vendas_com_nota_fiscal_emitida()

        context = {
            'media_valor': media_valor,
            'media_desconto': media_desconto,
            'menor_valor_venda': menor_valor_venda,
            'maior_valor_venda': maior_valor_venda,
            'quantidade_total_vendas': quantidade_total_vendas,
            'quantidade_total_vendas_com_nota_fiscal_emitida': quantidade_total_vendas_com_nota_fiscal_emitida
        }
        
        return render(
            request,
            'vendas/dashboard.html',
            context
        )
