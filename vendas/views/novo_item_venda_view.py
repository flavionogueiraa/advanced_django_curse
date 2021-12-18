'''
Shift + Alt + O para organizar as importações (vs code)
'''

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic.base import View

from ..models import ItemVenda


class NovoItemVendaView(LoginRequiredMixin, View):
    def get(self, request):
        pass

    def post(self, request, id_venda):
        context = {}
        item = get_object_or_404(ItemVenda, venda_id=id_venda)
