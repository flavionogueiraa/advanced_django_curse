'''
Favor colocar as importações em ordem alfabética para uma melhor organização
'''

from .cliente_admin import ClienteAdmin
from .documento_admin import DocumentoAdmin
from .venda_admin import VendaAdmin

__all__ = [
    ClienteAdmin,
    DocumentoAdmin,
    VendaAdmin,
]