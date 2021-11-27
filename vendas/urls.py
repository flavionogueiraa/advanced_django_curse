'''
Shift + Alt + O para organizar as importações (vs code)
'''

from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import DashboardView

urlpatterns = [
    path('dashboard/', login_required(DashboardView.as_view()), name='dashboard_view'),
]
