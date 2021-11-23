from django.apps import AppConfig


class AppModeloConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_modelo'

    def ready(self):
        from app_modelo import signals
