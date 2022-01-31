#Shift + Alt + O para organizar as importações (vs code)

from .cliente_admin import ClienteAdmin
from .documento_admin import DocumentoAdmin

__all__ = [
    ClienteAdmin,
    DocumentoAdmin,
]
