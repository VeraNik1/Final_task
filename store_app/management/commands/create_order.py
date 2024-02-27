from django.core.management.base import BaseCommand
from django.core.serializers import json
from store_app.models import User, Product, Order
import json

class Command(BaseCommand):
    help = "Create order"

    def add_arguments(self, parser):
        parser.add_argument("User_id", type=int, help="User ID")
        parser.add_argument('-p', '--Product_id', nargs='+', help="User ID", required=True)

    def handle(self, *args, **kwargs):
        user_id = kwargs.get('User_id')
        product_id: list = kwargs.get('Product_id')

        user = User.objects.filter(pk=user_id).first()

        order = Order(customer=user, is_deleted=False)
        total_price = 0
        for pk in product_id:
            product = Product.objects.filter(pk=pk).first()
            if product.quantity > 0:
                total_price += float(product.price)
                product.quantity -= 1
                product.save()
                order.total_price = total_price
                order.save()
                order.products.add(product)

            else:
                self.stdout.write(f'product {product.name} is out of stock')
        if total_price == 0:
            order.remove()


