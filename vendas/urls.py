'''
Shift + Alt + O para organizar as importações (vs code)
'''

from django.urls import path

from .views import DashboardView

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard_view'),
]
