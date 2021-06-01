'''
Favor colocar os nomes das importações em ordem alfabética para uma melhor organização
'''

from django.http import HttpResponse

def hello(request):
    return HttpResponse('Hello, World!')

def articles(request, year=None):
    return HttpResponse('O ano enviado foi {}'.format(year))