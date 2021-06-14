'''
Favor colocar as importações em ordem alfabética para uma melhor organização
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