from django.core.management.base import BaseCommand
from store_app.models import User


class Command(BaseCommand):
    help = "Show all users"

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        for user in users:
            if not user.is_deleted:
                self.stdout.write(f'id {user.id} {user}')
