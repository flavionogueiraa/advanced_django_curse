'''
Shift + Alt + O para organizar as importações (vs code)
'''
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('clientes/', include('clientes.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
