from django.core.management.base import BaseCommand
from store_app.models import User, Product, Order


class Command(BaseCommand):
    help = "Show all orders"

    def handle(self, *args, **kwargs):
        orders = Order.objects.all()
        for order in orders:
            if not order.is_deleted:
                self.stdout.write(f'id {order.id} - {order}')
