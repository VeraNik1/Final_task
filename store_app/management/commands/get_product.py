from django.core.management.base import BaseCommand
from store_app.models import Product


class Command(BaseCommand):
    help = "Get product by ID"

    def add_arguments(self, parser):
        parser.add_argument("pk", type=int, help="User ID")

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        product = Product.objects.filter(pk=pk).first()
        self.stdout.write(f'{product}')
