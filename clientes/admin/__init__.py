'''
Shift + Alt + O para organizar as importações (vs code)
'''

from .cliente_admin import ClienteAdmin
from .documento_admin import DocumentoAdmin
from .item_venda_admin import ItemVendaAdmin
from .produto_admin import ProdutoAdmin
from .venda_admin import VendaAdmin

__all__ = [
    ClienteAdmin,
    DocumentoAdmin,
    ItemVendaAdmin,
    ProdutoAdmin,
    VendaAdmin,
]
