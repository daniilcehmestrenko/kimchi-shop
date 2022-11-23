from .models import Categories
from cart.forms import CartAddProductForm


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        categories = Categories.objects.all()
        context['categories'] = categories
        context['cart_form'] = CartAddProductForm

        return context
