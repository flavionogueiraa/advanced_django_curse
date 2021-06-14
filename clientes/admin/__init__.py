'''
Favor colocar as importações em ordem alfabética para uma melhor organização
'''

from .cliente_admin import ClienteAdmin
from .documento_admin import DocumentoAdmin

__all__ = [
    ClienteAdmin,
    DocumentoAdmin,
]