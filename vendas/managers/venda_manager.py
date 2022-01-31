__author__ = "Francisco Flávio Nogueira da Silva"
__copyright__ = "Copyright 2021, Flávio Silva"
__credits__ = ["Flávio Silva"]
__version__ = "1.0"
__maintainer__ = "Francisco Flávio Nogueira da Silva"
__email__ = "flavio.nogueira.profissional@gmail.com"
__status__ = "Production"

#Shift + Alt + O para organizar as importações (vs code)

from django.db import models
from django.db.models import Avg, Max, Min


class VendaManager(models.Manager):
    '''
    Classe para definir as funções que iremos necessitar para as nossas vendas
    '''
    
    def media(query):
        return query.all().aggregate(
            valor_medio=Avg('total')
        )['valor_medio'] or 0

    def media_desconto(query):
        return query.all().aggregate(
            valor_medio=Avg('desconto')
        )['valor_medio'] or 0

    def menor_valor_venda(query):
        return query.all().aggregate(
            menor_valor=Min('total')
        )['menor_valor'] or 0

    def maior_valor_venda(query):
        return query.all().aggregate(
            maior_valor=Max('total')
        )['maior_valor'] or 0

    def quantidade_total_vendas(query):
        return query.all().count()

    def quantidade_total_vendas_com_nota_fiscal_emitida(query):
        return query.filter(
            nota_fiscal_emitida=True
        ).count()
