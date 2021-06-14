__author__ = "Francisco Flávio Nogueira da Silva"
__copyright__ = "Copyright 2021, Flávio Silva"
__credits__ = ["Flávio Silva"]
__version__ = "1.0"
__maintainer__ = "Francisco Flávio Nogueira da Silva"
__email__ = "flavio.nogueira.profissional@gmail.com"
__status__ = "Production"

'''
Favor colocar as importações em ordem alfabética para uma melhor organização
'''

from django.db import models

class Documento(models.Model):
    '''
    Classe para guardar os documentos dos clientes
    '''

    numero_documento = models.CharField(
        verbose_name='Número do documento',
        max_length=70
    )

    def __str__(self):
        return self.numero_documento
    
    class Meta:
        app_label='clientes'
        verbose_name='Documento'
        verbose_name_plural='Documentos'