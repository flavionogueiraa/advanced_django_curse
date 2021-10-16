'''
Shift + Alt + O para organizar as importações (vs code)
'''

from ..models import Person
from django.contrib import admin

@admin.register(Person)
class ClienteAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'first_name',
        'last_name',
        'age',
        'salary',
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