from django.apps import AppConfig


class RegisterConfig(AppConfig):
    name = 'Register'

    def ready(self):
        from Register import signals
