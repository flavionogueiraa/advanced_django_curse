'''
Shift + Alt + O para organizar as importações (vs code)
'''
import os
from django.core.wsgi import get_wsgi_application
from dj_static import Cling

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'curso_django.settings')

application = Cling(get_wsgi_application())
