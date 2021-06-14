'''
Favor colocar as importações em ordem alfabética para uma melhor organização
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