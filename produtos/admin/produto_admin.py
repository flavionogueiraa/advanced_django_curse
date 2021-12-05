'''
Shift + Alt + O para organizar as importações (vs code)
'''

from django.contrib import admin

from ..models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'descricao',
        'preco',
    ]
    
    search_fields = [
        'descricao',
        'preco',
    ]
