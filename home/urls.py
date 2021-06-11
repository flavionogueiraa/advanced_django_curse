'''
Favor colocar os nomes das importações em ordem alfabética para uma melhor organização
'''

from .views import home
from .views import logout_view
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('logout/', logout_view, name='logout'),
]