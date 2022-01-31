#Shift + Alt + O para organizar as importações (vs code)

from django.contrib import admin

from ..models import ItemVenda


class ItemVendaInline(admin.TabularInline):
    model = ItemVenda
    
    extra = 1

    autocomplete_fields = [
        'produto',
    ]
