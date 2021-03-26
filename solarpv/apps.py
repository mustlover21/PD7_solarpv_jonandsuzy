from django.apps import AppConfig



class SolarpvConfig(AppConfig):
    name = 'solarpv'

    def ready(self):
        import solarpv.signals
