from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.models import User

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


class AuthorizeView(View):
    def get(self, request):
        return render(request, 'core/authorize.html')

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('core:profile')

        else:
            messages.error(request, 'Неправильно введён логин или пароль')
            return redirect('core:authorize')


class RegisterView(View):
    def get(self, request):
        return render(request, 'core/register.html')

    def post(self, request):
        if not request.user.is_anonymous:
            return redirect('core:catalogue')

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.create_user(username,
                                            email,
                                            password,
                                            first_name=first_name,
                                            last_name=last_name)
        except IntegrityError:
            messages.error(
                request,
                'Пользователь с данным логином уже существует. Попробуйте ввести другой логин.',
            )
            return redirect('core:register')

        login(request, user, backend='django.contrib.auth.backends.ModelBackend')

        return render(request, 'core/profile.html')


def logout_view(request):
    logout(request)

    return redirect('core:catalogue')


def profile(request):
    context = {
        'items': Item.objects.all(),
    }
    return render(request, 'core/profile.html', context)
