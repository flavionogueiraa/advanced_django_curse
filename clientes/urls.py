'''
Favor colocar as importações em ordem alfabética para uma melhor organização
'''

from .views import person_create
from .views import persons_list
from django.urls import path

urlpatterns = [
    path('create/', person_create, name='person_create'),
    path('list/', persons_list, name='persons_list'),
]