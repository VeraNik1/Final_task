from django.db import models
from django.db.models import BooleanField


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    reg_date = models.DateField(auto_now_add=True)
    password = models.CharField(max_length=25)
    is_deleted = BooleanField()

    def __str__(self):
        if self.is_deleted:
            return f'User was deleted'
        return f'Username: {self.name}, email: {self.email},  phone: {self.phone}, address: {self.address}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    quantity = models.IntegerField()
    is_deleted = BooleanField()

    def __str__(self):
        if self.is_deleted:
            return f'Product was deleted'
        return (f'Product name: {self.name}, price: {self.price},  description: {self.description}, '
                f'quantity: {self.quantity}')


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    order_date = models.DateField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    is_deleted = BooleanField()

    def __str__(self):
        if self.is_deleted:
            return f'Order was deleted'
        return (f'Customer: {self.customer.name}, total_price: {self.total_price},'
                f'order date: {self.order_date}')