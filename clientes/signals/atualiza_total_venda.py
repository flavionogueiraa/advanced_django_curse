'''
Shift + Alt + O para organizar as importações (vs code)
'''

from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from ..models import Venda


@receiver(m2m_changed, sender=Venda.produtos.through)
def atualiza_total(sender, instance, **kwargs):
    instance.atualiza_total()
