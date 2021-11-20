'''
Shift + Alt + O para organizar as importações (vs code)
'''

from django.contrib import admin

from ..models import Venda


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'numero_venda',
        'valor',
        'desconto',
        'impostos',
        'total',
        'pessoa',
    ]

    list_filter = [
        'pessoa__documento',
        'desconto',
    ]

    search_fields = [
        'numero_venda',
        'valor',
        'desconto',
        'impostos',
        'pessoa__first_name',
        'pessoa__last_name',
    ]

    autocomplete_fields = [
        'pessoa',
    ]

    filter_horizontal = [
        'produtos',
    ]
