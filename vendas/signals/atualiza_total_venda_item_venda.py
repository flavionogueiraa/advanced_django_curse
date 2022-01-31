#Shift + Alt + O para organizar as importações (vs code)

from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models import ItemVenda


@receiver(post_save, sender=ItemVenda)
def atualiza_total_venda_item_venda(sender, instance, **kwargs):
    instance.venda.save()
