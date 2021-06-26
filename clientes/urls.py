'''
Favor colocar as importações em ordem alfabética para uma melhor organização
'''

from .views import PersonCreateView
from .views import PersonDeleteView
from .views import person_delete
from .views import PersonDetailView
from .views import person_form
from .views import person_list
from .views import PersonList
from .views import person_update
from .views import PersonUpdateView
from django.contrib.auth.decorators import login_required
from django.urls import path

urlpatterns = [
    path('create/', person_form, name='person_form'),
    path('list/', person_list, name='person_list'),
    path('update/<int:id>/', person_update, name='person_update'),
    path('delete/<int:id>/', person_delete, name='person_delete'),

    path('list_cbv/', login_required(PersonList.as_view()), name='person_list_cbv'),
    path('detail_cbv/<int:pk>/', login_required(PersonDetailView.as_view()), name='person_detail_cbv'),
    path('create_cbv/', login_required(PersonCreateView.as_view()), name='person_create_cbv'),
    path('update_cbv/<int:pk>/', login_required(PersonUpdateView.as_view()), name='person_update_cbv'),
    path('person_delete_cbv/<int:pk>/', login_required(PersonDeleteView.as_view()), name='person_delete_cbv'),
]