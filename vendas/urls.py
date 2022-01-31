#Shift + Alt + O para organizar as importações (vs code)

from django.urls import path

from .views import DashboardView, NovoPedidoView

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard_view'),
    path('novo-pedido-view/', NovoPedidoView.as_view(), name='novo_pedido_view'),
]
