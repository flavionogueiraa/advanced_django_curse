'''
Favor colocar os nomes das importações em ordem alfabética para uma melhor organização
'''
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('clientes/', include('clientes.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
