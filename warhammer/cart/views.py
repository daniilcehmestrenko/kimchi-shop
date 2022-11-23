from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView

from shop.models import Orders
from shop.utils import DataMixin
from .forms import CartAddProductForm
from .cart import Cart


def cart_remove(request, slug):
    cart = Cart(request)
    product = get_object_or_404(Orders, slug=slug)
    cart.remove(product)

    return redirect('cart_detail')

def cart_add(request, slug):
    cart = Cart(request)
    product = get_object_or_404(Orders, slug=slug)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        data_form = form.cleaned_data
        cart.add(
            product,
            data_form['quantity'],
            data_form['update']
        )

    return redirect('cart_detail')

class CartDetail(DataMixin, TemplateView):
    template_name = 'cart/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        data = self.get_user_context()

        return context|data
