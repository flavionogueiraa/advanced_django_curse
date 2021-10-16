'''
Shift + Alt + O para organizar as importações (vs code)
'''

from ..models import Venda
from django.contrib import admin

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'numero_venda',
        'valor',
        'desconto',
        'impostos',
        'pessoa',
    ]

    list_filter = [
        'pessoa',
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