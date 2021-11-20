'''
Shift + Alt + O para organizar as importações (vs code)
'''

from django.contrib import admin

from ..models import Person


@admin.register(Person)
class ClienteAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'first_name',
        'last_name',
        'age',
        'salary',
        'possui_foto',
    ]

    list_filter = [
        'age',
    ]

    autocomplete_fields = [
        'documento',
    ]

    search_fields = [
        'id',
        'first_name',
        'last_name',
        'age',
        'salary',
    ]

    def possui_foto(self, obj):
        if obj and obj.foto:
            return 'Sim'
        else:
            return 'Não'
    possui_foto.short_description = 'Possui foto'