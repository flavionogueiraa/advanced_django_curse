'''
Favor colocar os nomes das importações em ordem alfabética para uma melhor organização
'''

from .views import home
from .views import Home3
from .views import logout_view
from django.urls import path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', home, name='home'),
    path('logout/', logout_view, name='logout'),
    path('home2/', TemplateView.as_view(template_name='home2.html'), name='home2'),
    path('home3/', Home3.as_view(template_name='home3.html'), name='home3'),
]