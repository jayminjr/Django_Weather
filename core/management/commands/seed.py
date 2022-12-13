from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.apps import apps


class Command(BaseCommand):
    help = "Seeds initial data for the application."

    def __init__(self):
        super().__init__()

    def handle(self, *args, **options):
        self.all_apps_make_migation()
        self.migrate()

    def all_apps_make_migation(self):
        for app in apps.get_app_configs():
            call_command("makemigrations", app.label)
            self.stdout.write("Created {} migration.".format(app.label))

    def migrate(self):
        call_command("migrate")
