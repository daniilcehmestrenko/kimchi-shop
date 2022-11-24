from django.contrib import admin

from .models import ProductOrder, ProductOrderItem


class ProductOrderItemInLine(admin.TabularInline):
    model = ProductOrderItem
    raw_id_fields = ['product']


class ProductOrderAdmin(admin.ModelAdmin):
    list_display = [
            'id', 'first_name', 'last_name',
            'email', 'adres', 'postal_code',
            'city', 'paid', 'created', 'updated'
        ]
    list_filter = ['paid', 'created', 'updated']

    inlines = [ProductOrderItemInLine]


admin.site.register(ProductOrder, ProductOrderAdmin)
