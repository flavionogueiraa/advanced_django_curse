'''
Shift + Alt + O para organizar as importações (vs code)
'''

from django import forms


class ItemVendaForm(forms.Form):
    item_venda_id = forms.IntegerField(label='ID do item_venda')
    quantidade= forms.IntegerField(label='Quantidade')
    desconto = forms.DecimalField(label='Desconto')
