from django.urls import path

from .views import CartDetail, cart_add, cart_remove


urlpatterns = [
    path('',
         CartDetail.as_view(),
         name='cart_detail'),
    path('add/<slug:slug>',
         cart_add,
         name='cart_add'),
    path('remove/<slug:slug>',
         cart_remove,
         name='cart_remove')
]
