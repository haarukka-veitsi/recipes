from django.shortcuts import render

from core.models import Item


def news(request):
    context = {
        'items': Item.objects.all(),
        'items_check': 'Hi, you fucked up'
    }
    return render(request, 'core/index.html', context=context)
