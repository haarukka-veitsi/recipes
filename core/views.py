from django.shortcuts import render, get_object_or_404

from core.models import Item, ItemIngredient, ItemStep


def catalogue(request):
    context = {
        'items': Item.objects.all(),
    }
    return render(request, 'core/index.html', context)


def item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    steps = ItemStep.objects.filter(item=item_id)
    ingredients = ItemIngredient.objects.filter(item=item_id)
    context = {
        'item': item,
        'steps': steps,
        'ingredients': ingredients,
    }
    return render(request, 'core/item.html', context)
