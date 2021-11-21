__author__ = "Francisco Flávio Nogueira da Silva"
__copyright__ = "Copyright 2021, Flávio Silva"
__credits__ = ["Flávio Silva"]
__version__ = "1.0"
__maintainer__ = "Francisco Flávio Nogueira da Silva"
__email__ = "flavio.nogueira.profissional@gmail.com"
__status__ = "Production"

'''
Shift + Alt + O para organizar as importações (vs code)
'''

from django.db import models

from .produto import Produto
from .venda import Venda


class ItemVenda(models.Model):
    '''
    Classe para fazer o relacionamento de vendas com produtos
    '''
    
    venda = models.ForeignKey(
        Venda,
        verbose_name='Venda',
        on_delete=models.CASCADE
    )

    produto = models.ForeignKey(
        Produto,
        verbose_name='Produto',
        on_delete=models.CASCADE
    )

    quantidade = models.FloatField(
        verbose_name='Quantidade',
        default=0
    )

    desconto = models.DecimalField(
        verbose_name='Desconto',
        max_digits=5, decimal_places=2,
        default=0,
        blank=True, null=True
    )

    def __str__(self):
        return 'Item {} - Venda {}'.format(self.id, self.venda)
    
    class Meta:
        app_label='clientes'
        verbose_name='Item da venda'
        verbose_name_plural='Itens da venda'
