'''
Favor colocar as importações em ordem alfabética para uma melhor organização
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

    search_fields = [
        'id',
        'first_name',
        'last_name',
        'age',
        'salary',
    ]