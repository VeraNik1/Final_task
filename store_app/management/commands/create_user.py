from django.core.management.base import BaseCommand
from store_app.models import User


class Command(BaseCommand):
    help = "Create User"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str, help="User Name")
        parser.add_argument("email", type=str, help="User email")
        parser.add_argument("password", type=str, help="User password")
        parser.add_argument("phone", type=str, help="phone email")
        parser.add_argument("address", type=str, help="User address")

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        email = kwargs.get('email')
        password = kwargs.get('password')
        phone = kwargs.get('phone')
        address = kwargs.get('address')

        user = User(name=name, email=email, password=password, phone=phone, address=address, is_deleted=False)
        user.save()
        self.stdout.write(f'{user}')
