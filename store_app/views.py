from datetime import date, timedelta
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView, FormView
from .forms import ProductEditForm
from .models import User, Product, Order
from django.contrib import messages



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


def edit_product(request, product_id=None):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':

        form = ProductEditForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Данные успешно изменены!')
            return redirect('index')
        else:
            messages.error(request, 'Форма заполнена неверно!')
            return render(request, 'store_app/edit_form.html', context={'form': form})
    else:
        form = ProductEditForm(instance=product)
    return render(request, 'store_app/edit_form.html', context={'form': form})


def users_view(request):
    clients_ = User.objects.all().filter(is_deleted=False)
    return render(request, 'store_app/users.html', {'clients': clients_})


def products_view(request):
    products_ = Product.objects.all().filter(is_deleted=False)
    return render(request, 'store_app/products.html', {'products': products_})


def orders_view(request):
    orders = Order.objects.filter(is_deleted=False)
    context = {'orders': orders}
    return render(request, 'store_app/orders.html', context)



def get_order_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    context = {'order': order}
    return render(request, 'store_app/order.html', context=context)



def get_product_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {'product': product}
    return render(request, 'store_app/product.html', context=context)


def get_user_view(request, user_id):
    client = get_object_or_404(User, id=user_id)
    context = {'client': client}
    return render(request, 'store_app/user.html', context=context)
