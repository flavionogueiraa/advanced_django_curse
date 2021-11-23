'''
Shift + Alt + O para organizar as importações (vs code)
'''

from django.contrib import admin

from ..models import ItemVenda


@admin.register(ItemVenda)
class ItemVendaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'venda',
        'produto',
        'quantidade',
    ]

    list_filter = [
        'venda',
        'produto',
    ]

    search_fields = [
        'id',
        'venda__numero_venda',
        'produto__descricao',
        'quantidade',
    ]

    autocomplete_fields = [
        'venda',
        'produto',
    ]
