from django.urls import path

from .views import (CreateComment, OrderDetail,
                    OrderList, OrderByCategoryList,
                    cart_detail, cart_add, cart_remove)


urlpatterns = [
    path('',
        OrderList.as_view(),
        name='home'),
    path('category/<slug:slug>',
         OrderByCategoryList.as_view(),
         name='category'),
    path('order/<slug:slug>',
         OrderDetail.as_view(),
         name='order'),
    path('create/<int:pk>',
         CreateComment.as_view(),
         name='create_comment'),
    path('cart/',
         cart_detail,
         name='cart_detail'),
    path('cart/add/<slug:slug>',
         cart_add,
         name='cart_add'),
    path('cart/remove/<slug:slug>',
         cart_remove,
         name='cart_remove')
]
