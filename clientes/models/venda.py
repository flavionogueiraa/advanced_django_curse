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

from .cliente import Person
from .produto import Produto
from django.db import models

class Venda(models.Model):
    '''
    Classe que guarda as vendas que os clientes fazem
    '''

    numero_venda = models.CharField(
        verbose_name='Número da venda',
        max_length=70
    )

    valor = models.DecimalField(
        verbose_name='Valor',
        max_digits=7, decimal_places=2
    )

    desconto = models.DecimalField(
        verbose_name='Desconto',
        max_digits=5, decimal_places=2
    )

    impostos = models.DecimalField(
        verbose_name='Impostos',
        max_digits=4, decimal_places=2
    )

    pessoa = models.ForeignKey(
        Person,
        verbose_name='Pessoa',
        blank=True, null=True,
        on_delete=models.SET_NULL
    )

    produtos = models.ManyToManyField(
        Produto,
        verbose_name='Produtos',
        blank=True
    )

    def __str__(self):
        return self.numero_venda
    
    class Meta:
        app_label='clientes'
        verbose_name='Venda'
        verbose_name_plural='Vendas'