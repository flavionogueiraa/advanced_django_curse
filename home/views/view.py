'''
Favor colocar as importações em ordem alfabética para uma melhor organização
'''

from django.shortcuts import HttpResponse, render
from django.views.generic.base import View

class MyView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        
        return render(
            request,
            'home/view.html',
            context
        )
    
    def post(self, request, *args, **kwargs):
        return HttpResponse('Post')