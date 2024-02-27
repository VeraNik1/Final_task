from datetime import date, timedelta
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, FormView

from .models import User, Product, Order


def index(request):
    return render(request, "store_app/index.html")


class ClientOrders(TemplateView):
    template_name = "store_app/client_statistics.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(User, pk=context['user_id'])
        orders = Order.objects.filter(customer=user).filter(is_deleted=False).order_by('id')
        context['user'] = user
        context['orders'] = orders
        return context


class OrderedProducts(TemplateView):
    template_name = "store_app/orders_statistics.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client = get_object_or_404(User, pk=context['user_id'])
        context['user'] = client
        orders = Order.objects.filter(customer=client).filter(is_deleted=False).order_by('id')
        cur_date = date.today()
        products_for_week = {}
        products_for_month = {}
        products_for_year = {}
        for order in orders:
            for item in order.products.all():
                if order.order_date > (cur_date - timedelta(days=7)):
                    products_for_week[f'{item.name}'] = item
                if order.order_date > (cur_date - timedelta(days=30)):
                    products_for_month[f'{item.name}'] = item
                if order.order_date > (cur_date - timedelta(days=365)):
                    products_for_year[f'{item.name}'] = item
        context['products_for_week'] = products_for_week
        context['products_for_month'] = products_for_month
        context['products_for_year'] = products_for_year
        return context
