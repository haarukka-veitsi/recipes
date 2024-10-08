from django.contrib import admin

from core.models import Item, ItemCategory


@admin.register(Item)
class Item(admin.ModelAdmin):
    list_display = ('title',)

    @admin.display(description='title')
    def title(self, obj):
        return f'{obj.name} ({obj.id})'


@admin.register(ItemCategory)
class ItemCategory(admin.ModelAdmin):
    list_display = ('category',)

    @admin.display(description='category')
    def category(self, obj):
        return f'{obj.name} ({obj.id})'
