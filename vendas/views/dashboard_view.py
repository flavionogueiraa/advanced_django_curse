'''
Shift + Alt + O para organizar as importações (vs code)
'''

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseForbidden
from django.shortcuts import render
from django.views import View

from ..models import Venda


class DashboardView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('vendas.visualizar_dashboard'):
            return HttpResponseForbidden()
        
        return super(DashboardView, self).dispatch(request, *args, **kwargs)

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
