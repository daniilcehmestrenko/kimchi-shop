from django.urls import path

from .views import (CreateComment, OrderDetail,
                    OrderList, OrderByCategoryList)


urlpatterns = [
    path(
        '',
        OrderList.as_view(),
        name='home'
    ),
    path(
        'category/<slug:slug>',
        OrderByCategoryList.as_view(),
        name='category'
    ),
    path(
        'order/<slug:slug>',
        OrderDetail.as_view(),
        name='order'
    ),
    path(
        'create/<int:pk>',
        CreateComment.as_view(),
        name='create_comment'
    ),
]
