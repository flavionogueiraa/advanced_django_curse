'''
Favor colocar as importações em ordem alfabética para uma melhor organização
'''

from .home import home
from .home3 import Home3
from .logout import logout_view
from .view import MyView

__all__ = [
    home,
    Home3,
    logout_view,
    MyView,
]