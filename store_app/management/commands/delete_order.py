from django.core.management.base import BaseCommand
from store_app.models import User, Product, Order



class Command(BaseCommand):
    help = "Delete order by ID"

    def add_arguments(self, parser):
        parser.add_argument("pk", type=int, help="Order ID")
    def handle (self, *args, **kwargs):

        pk = kwargs.get('pk')
        order = Order.objects.filter(pk=pk).first()
        if order is not None:
            order.is_deleted = True
            order.save()
        self.stdout.write(f'{order}')