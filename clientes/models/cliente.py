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

class Person(models.Model):
    '''
    Classe que serve para guardar uma pessoa 
    '''
    first_name = models.CharField(
        verbose_name='First name',
        max_length=70
    )

    last_name = models.CharField(
        verbose_name='Last name',
        max_length=70
    )

    age = models.IntegerField(
        verbose_name='Age'
    )

    salary = models.DecimalField(
        verbose_name='Salary',
        max_digits=7, decimal_places=2
    )

    foto = models.ImageField(
        verbose_name='Foto',
        upload_to='fotos_clientes/',
        null=True, blank=True
    )

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    class Meta:
        app_label='clientes'
        verbose_name='Cliente'
        verbose_name_plural='Clientes'