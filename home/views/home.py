'''
Favor colocar as importações em ordem alfabética para uma melhor organização
'''

from django.shortcuts import render

def home(request):
    context = {}

    return render(
        request,
        'home/home.html',
        context
    )