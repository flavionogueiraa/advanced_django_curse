'''
Shift + Alt + O para organizar as importações (vs code)
'''

from django.shortcuts import render


def home(request):
    context = {}

    return render(
        request,
        'home/home.html',
        context
    )
