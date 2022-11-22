from django.contrib import admin
from .models import Categories, Comments, Orders, Tags


class CatergoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'user_name', 'content']
    list_display_links = ('email',)
    search_fields = ('content',)

class OrderAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name_tag',)}

admin.site.register(Categories, CatergoryAdmin)
admin.site.register(Comments, CommentAdmin)
admin.site.register(Orders, OrderAdmin)
admin.site.register(Tags, TagAdmin)
