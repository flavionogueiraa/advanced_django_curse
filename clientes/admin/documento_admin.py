#Shift + Alt + O para organizar as importações (vs code)

from ..models import Documento
from django.contrib import admin

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'numero_documento',
    ]

    search_fields = [
        'numero_documento',
    ]