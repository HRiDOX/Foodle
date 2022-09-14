from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
 #Ready function is responsible for making the signals to work in the signal
    def ready(self):
        import accounts.signals