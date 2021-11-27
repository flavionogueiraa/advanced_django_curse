'''
Shift + Alt + O para organizar as importações (vs code)
'''

from django.db.models import Avg
from django.shortcuts import render
from django.views import View

from ..models import Venda


class DashboardView(View):
    def get(self, request):
        media = Venda.objects.all().aggregate(
            valor_total=Avg('total')
        )['valor_total'] or 0
        
        context = {
            'media': media,
        }
        
        return render(
            request,
            'vendas/dashboard.html',
            context
        )
