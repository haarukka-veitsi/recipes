from django.contrib import admin

from core.models import Item, ItemCategory, ItemIngredient, ItemStep, UserImage


@admin.register(Item)
class Item(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(ItemCategory)
class ItemCategory(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(ItemIngredient)
class ItemIngredient(admin.ModelAdmin):
    list_display = ('id', 'item', 'name',)


@admin.register(ItemStep)
class ItemStep(admin.ModelAdmin):
    list_display = ('id', 'item', 'number')


@admin.register(UserImage)
class UserImage(admin.ModelAdmin):
    list_display = ('id', 'user', 'image')