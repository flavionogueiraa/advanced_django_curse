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

from time import time

from clientes.models import Person
from django.db import models
from django.db.models import DecimalField, F, Sum

from ..managers import VendaManager


class Venda(models.Model):
    '''
    Classe que guarda as vendas que os clientes fazem
    '''

    numero_venda = models.CharField(
        verbose_name='Número da venda',
        max_length=70
    )

    total = models.DecimalField(
        verbose_name='Total',
        max_digits=7, decimal_places=2,
        blank=True, null=True
    )

    desconto = models.DecimalField(
        verbose_name='Desconto',
        default=0,
        max_digits=5, decimal_places=2
    )

    impostos = models.DecimalField(
        verbose_name='Impostos',
        default=0,
        max_digits=4, decimal_places=2
    )

    pessoa = models.ForeignKey(
        Person,
        verbose_name='Pessoa',
        blank=True, null=True,
        on_delete=models.SET_NULL
    )

    nota_fiscal_emitida = models.BooleanField(
        verbose_name='Nota fiscal emitida',
        default=False
    )

    def atualiza_total(self):
        total_itens_venda = self.itemvenda_set.all().aggregate(
            total = Sum(
                (F('produto__preco') * F('quantidade')) - F('desconto'),
                output_field=DecimalField()
            )
        )['total'] or 0

        total = total_itens_venda - self.desconto - self.impostos
        self.total = total
        self.save()
    
    objects = VendaManager()

    def __str__(self):
        return self.numero_venda
    
    class Meta:
        app_label='vendas'
        verbose_name='Venda'
        verbose_name_plural='Vendas'
        permissions = [
            ('alterar_nota_fiscal', 'Pode alterar o status de uma nota fiscal'),
        ]
