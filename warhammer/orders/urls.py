from django.urls import path

from .views import OrderCreate, order_created

urlpatterns = [
        path(
            'create/',
            OrderCreate.as_view(),
            name='order_create'
        ),
        path(
            'created/<int:pk>',
            order_created,
            name='created',
        ),
    ]
