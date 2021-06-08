'''
Favor colocar as importações em ordem alfabética para uma melhor organização
'''

from .person_create import person_create
from .persons_list import persons_list

__all__ = [
    person_create,
    persons_list,
]