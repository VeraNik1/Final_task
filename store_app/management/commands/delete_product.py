from django.core.management.base import BaseCommand
from store_app.models import Product


class Command(BaseCommand):
    help = "Delete product by ID"

    def add_arguments(self, parser):
        parser.add_argument("pk", type=int, help="User ID")

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.filter(pk=pk).first()
        if product is not None:
            product.is_deleted = True
            product.save()
        self.stdout.write(f'{product}')
