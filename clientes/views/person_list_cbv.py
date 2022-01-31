#Shift + Alt + O para organizar as importações (vs code)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from ..models import Person


class PersonList(LoginRequiredMixin, ListView):
    model = Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cria_mensagem_bem_vindo(self.request, context)
        return context



#ANCHOR funções auxiliares
def cria_mensagem_bem_vindo(request, context):
    ja_acessou = request.session.get('ja_acessou', None)
    if ja_acessou:
        context.update({
            'mensagem': 'Olá {}, bem vindo de volta!'.format(request.user)
        })
    else:
        context.update({
            'mensagem': 'Olá {}, bem vindo ao nosso sistema pela primeira vez!'.format(request.user)
        })
    
    atualiza_ja_acessou(request, ja_acessou)

def atualiza_ja_acessou(request, ja_acessou):
    if not ja_acessou:
        request.session.update({
            'ja_acessou': True
        })
