from django.contrib import admin

from .models import Item, Menu


class ItemInline(admin.StackedInline):
    model = Item


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug')
    inlines = [
        ItemInline,
    ]
