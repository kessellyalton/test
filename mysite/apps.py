from django.apps import AppConfig


class MysiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mysite'

    def ready(self):
        import mysite.dash_apps  # Import the dash_apps module




