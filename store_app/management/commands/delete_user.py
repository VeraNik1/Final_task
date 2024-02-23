from django.core.management.base import BaseCommand
from store_app.models import User


class Command(BaseCommand):
    help = "Delete user by ID"

    def add_arguments(self, parser):
        parser.add_argument("pk", type=int, help="User ID")

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.filter(pk=pk).first()
        if user is not None:
            user.is_deleted = True
            user.save()
        self.stdout.write(f'{user}')
