from django.core.management.base import BaseCommand
from store_app.models import Product


class Command(BaseCommand):
    help = "Show all products"

    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        for item in products:
            if not item.is_deleted:
                self.stdout.write(f'{item}')