'''
Favor colocar os nomes das importações em ordem alfabética para uma melhor organização
'''

from django.views.generic.base import TemplateView

class Home3(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['minha_variavel'] = 'Olá, seja bem vindo curso de Django advanced'
        return context