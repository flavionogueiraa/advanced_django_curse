'''
Favor colocar os nomes das importações em ordem alfabética para uma melhor organização
'''
from .views import articles
from .views import fname
from .views import fname2
from .views import hello

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('person/', include('clientes.urls')),
    path('articles/<int:year>/', articles),
    path('pessoa/<str:nome>/', fname2),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
