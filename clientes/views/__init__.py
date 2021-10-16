'''
Shift + Alt + O para organizar as importações (vs code)
'''

from .person_create_cbv import PersonCreateView
from .person_delete import person_delete
from .person_delete_cbv import PersonDeleteView
from .person_detail import PersonDetailView
from .person_form import person_form
from .person_list import person_list
from .person_list_cbv import PersonList
from .person_update_cbv import PersonUpdateView
from .person_update import person_update

__all__ = [
    PersonCreateView,
    PersonDeleteView,
    person_delete,
    PersonDetailView,
    person_form,
    person_list,
    PersonList,
    PersonUpdateView,
    person_update,
]