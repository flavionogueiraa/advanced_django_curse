'''
Shift + Alt + O para organizar as importações (vs code)
'''

from ..models import Produto
from django.contrib import admin

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