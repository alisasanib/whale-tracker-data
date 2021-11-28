from django.apps import AppConfig


class ApiAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api_app'

    def ready(self):
        print("Starting Scheduler ...")
        from .whale_scheduler import whale_updater
        whale_updater.start()
