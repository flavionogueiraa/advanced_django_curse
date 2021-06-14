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

class Produto(models.Model):
    '''
    Classe que contém os produtos das vendas
    '''

    descricao = models.CharField(
        verbose_name='Descrição',
        max_length=70
    )

    preco = models.DecimalField(
        verbose_name='Preço',
        max_digits=8, decimal_places=2
    )

    def __str__(self):
        return self.descricao
    
    class Meta:
        app_label='clientes'
        verbose_name='Produto'
        verbose_name_plural='Produtos'