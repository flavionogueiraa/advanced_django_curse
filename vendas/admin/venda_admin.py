#Shift + Alt + O para organizar as importações (vs code)

from django.contrib import admin

from ..actions.venda_actions import cancelar_nota_fiscal, emitir_nota_fiscal
from ..models import Venda
from .item_venda_inline import ItemVendaInline


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'numero_venda',
        'total',
        'pessoa',
        'nota_fiscal_emitida',
    ]

    list_filter = [
        'pessoa__documento',
        'desconto',
    ]

    search_fields = [
        'numero_venda',
        'total',
        'desconto',
        'impostos',
        'pessoa__first_name',
        'pessoa__last_name',
    ]

    autocomplete_fields = [
        'pessoa',
    ]

    readonly_fields = [
        'total',
    ]

    actions = [
        cancelar_nota_fiscal,
        emitir_nota_fiscal,
    ]

    inlines = [
        ItemVendaInline,
    ]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if not request.user.has_perm('vendas.alterar_nota_fiscal'):
            actions.pop('cancelar_nota_fiscal')
            actions.pop('emitir_nota_fiscal')
        
        return actions