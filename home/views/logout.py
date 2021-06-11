'''
Favor colocar as importações em ordem alfabética para uma melhor organização
'''

from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.shortcuts import redirect

def logout_view(request):
    logout(request)

    return redirect(reverse_lazy('home'))