from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from shop.utils import DataMixin
from .models import ProductOrderItem
from .forms import ProductOrderForm
from cart.cart import Cart


def order_created(request, pk):

    return render(
            request,
            'orders/created.html',
            {'pk': pk}
        )

class OrderCreate(DataMixin, TemplateView):
    template_name = 'orders/create.html'

    def add_product_in_order(self, item, product_order):
        ProductOrderItem.objects.create(
                product_order=product_order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
            )

    def post(self, request):
        form = ProductOrderForm(request.POST)
        cart = Cart(request)
        if form.is_valid():
            product_order = form.save()
            for item in cart:
                self.add_product_in_order(item, product_order)

            cart.clear()

        return redirect('created', product_order.pk)



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_user_context()
        context['form'] = ProductOrderForm
        context['cart'] = Cart(self.request)
        
        return context|data
