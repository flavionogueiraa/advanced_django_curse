'''
Favor colocar os nomes das importações em ordem alfabética para uma melhor organização
'''
from .views import articles
from .views import fname
from .views import hello

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('articles/<int:year>/', articles),
    path('pessoa/<str:nome>/', fname),
]
