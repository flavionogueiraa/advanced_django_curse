'''
Shift + Alt + O para organizar as importações (vs code)
'''

from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models import Venda


@receiver(post_save, sender=Venda)
def atualiza_total_venda(sender, instance, **kwargs):
    post_save.disconnect(atualiza_total_venda, sender=Venda)
    instance.atualiza_total()
    post_save.connect(atualiza_total_venda, sender=Venda)
