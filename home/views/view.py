'''
Shift + Alt + O para organizar as importações (vs code)
'''

from datetime import datetime, timedelta

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponse, render
from django.views.generic.base import View


class MyView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        context = {}
        response = render(
            request,
            'home/view.html',
            context
        )

        seta_cookie(response, calcular_ano_que_vem())
        imprime_cookie(request)
        return response
    
    def post(self, request, *args, **kwargs):
        return HttpResponse('Post')



# ANCHOR funções auxiliares
def calcular_ano_que_vem():
    return datetime.today() + timedelta(days=365)

def seta_cookie(response, data_expiracao):
    response.set_cookie(
        'cookie_teste',
        'valor do cookie de testes',
        expires=data_expiracao
    )

def imprime_cookie(request):
    cookie = request.COOKIES.get('cookie_teste', None)
    if cookie:
        print(cookie)
