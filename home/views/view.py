'''
Shift + Alt + O para organizar as importações (vs code)
'''

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponse, render
from django.views.generic.base import View


class MyView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        context = {}
        
        return render(
            request,
            'home/view.html',
            context
        )
    
    def post(self, request, *args, **kwargs):
        return HttpResponse('Post')
