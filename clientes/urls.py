'''
Favor colocar as importações em ordem alfabética para uma melhor organização
'''

from .views import persons_list
from django.urls import path

urlpatterns = [
    path('list/', persons_list, name='persons_list'),
]