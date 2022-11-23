from django.views.generic import ListView, DetailView, CreateView

from .forms import AddCommentForm
from .models import Orders, Comments
from .utils import DataMixin


class CreateComment(CreateView):
    model = Comments
    form_class = AddCommentForm

    def form_valid(self, form):
        form.instance.order_id = self.kwargs.get('pk')
        self.object = form.save()

        return super().form_valid(form)

    def get_success_url(self):
        return self.object.order.get_absolute_url()


class OrderDetail(DataMixin, DetailView):
    model = Orders
    template_name = 'shop/order_detail.html'
    context_object_name = 'order'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_user_context()
        context['title'] = context['order'].title
        context['form'] = AddCommentForm()

        return context|data


class OrderList(DataMixin, ListView):
    model = Orders
    template_name = 'shop/orders.html'
    context_object_name = 'orders'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_user_context(title='Главная страница')

        return context|data

    def get_queryset(self):
        return (Orders.objects
                .prefetch_related('tags')
                .filter(is_published=True
            ))


class OrderByCategoryList(DataMixin, ListView):
    model = Orders
    template_name = 'shop/orders.html'
    context_object_name = 'orders'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_user_context(title=context['orders'][0]
                                     .category.name)

        return context|data

    def get_queryset(self):

        return (Orders.objects
                .filter(
                category__slug=self.kwargs['slug'],
                is_published=True
            ))
