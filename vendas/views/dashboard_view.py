'''
Shift + Alt + O para organizar as importações (vs code)
'''

from django.db.models import Avg, Max, Min
from django.shortcuts import render
from django.views import View

from ..models import Venda


class DashboardView(View):
    def get(self, request):
        media_valor = Venda.objects.all().aggregate(
            valor_medio=Avg('total')
        )['valor_medio'] or 0
        
        media_desconto = Venda.objects.all().aggregate(
            valor_medio=Avg('desconto')
        )['valor_medio'] or 0

        menor_venda = Venda.objects.all().aggregate(
            menor_valor=Min('total')
        )['menor_valor'] or 0

        maior_venda = Venda.objects.all().aggregate(
            maior_valor=Max('total')
        )['maior_valor'] or 0

        total_vendas = Venda.objects.all().count()
        
        total_vendas_com_nota_fiscal_emitida = Venda.objects.filter(
            nota_fiscal_emitida=True
        ).count()

        context = {
            'media_valor': media_valor,
            'media_desconto': media_desconto,
            'menor_venda': menor_venda,
            'maior_venda': maior_venda,
            'total_vendas': total_vendas,
            'total_vendas_com_nota_fiscal_emitida': total_vendas_com_nota_fiscal_emitida
        }
        
        return render(
            request,
            'vendas/dashboard.html',
            context
        )
