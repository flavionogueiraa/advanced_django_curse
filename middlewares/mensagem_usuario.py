'''
Shift + Alt + O para organizar as importações (vs code)
'''

class MensagemUsuario(object):
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Código que é executado antes da view ser
        # chamada e depois do último middleware antes desse
        
        response = self.get_response(request)

        # Código depois que é executado depois que
        # a view é chamada

        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated:
            mensagem = 'Olá {}, bom dia!'.format(request.user)
        else:
            mensagem =  'Olá, bom dia!'
        
        request.session['mensagem'] = mensagem
