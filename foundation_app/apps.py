# foundation_app/apps.py

from django.apps import AppConfig

class FoundationAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'foundation_app' # <--- ENSURE THIS IS 'foundation_app'
    verbose_name = 'Foundation Application' # Optional: A more human-readable name for the admin
