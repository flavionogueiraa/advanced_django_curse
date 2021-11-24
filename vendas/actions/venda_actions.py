'''
Shift + Alt + O para organizar as importações (vs code)
'''

def emitir_nota_fiscal(model_admin, request, queryset):
    queryset.update(nota_fiscal_emitida=True)

def cancelar_nota_fiscal(model_admin, request, queryset):
    queryset.update(nota_fiscal_emitida=False)
