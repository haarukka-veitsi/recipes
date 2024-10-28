from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.forms import modelformset_factory

from core.models import Item, ItemIngredient, ItemStep
from core.forms import ItemForm, ItemIngredientForm, ItemStepForm


class CatalogueView(View):
    def get(self, request):
        context = {
            'items': Item.objects.all().order_by('-id'),
        }
        return render(request, 'core/index.html', context)


class ItemView(View):
    def get(self, request, item_id):
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


class LogoutView(View):
    def get(self, request):
        logout(request)

        return redirect('core:catalogue')


class ProfileView(View):
    def get(self, request):
        context = {
            'items': Item.objects.all().order_by('-id'),
        }
        return render(request, 'core/profile.html', context)


class AddItemView(View):
    def get(self, request):
        step = request.session.get('form_step', 1)

        if step == 1:
            form = ItemForm()
        elif step == 2:
            form = ItemIngredientForm()
        elif step == 3:
            form = ItemStepForm()
        else:
            return redirect('core:profile')

        return render(request, 'core/add_item.html', {'form': form, 'step': step})

    def post(self, request):
        step = request.session.get('form_step', 1)

        if step == 1:
            form = ItemForm(request.POST)
            if form.is_valid():
                item = form.save()
                request.session['item_id'] = item.id
                request.session['form_step'] = 2
                return redirect('core:add_item')

        elif step == 2:
            form = ItemIngredientForm(request.POST)
            if form.is_valid():
                ingredient = form.save(commit=False)
                ingredient.item_id = request.session.get('item_id')
                ingredient.save()
                request.session['form_step'] = 3
                return redirect('core:add_item')

        elif step == 3:
            form = ItemStepForm(request.POST)
            if form.is_valid():
                step_instance = form.save(commit=False)
                step_instance.item_id = request.session.get('item_id')
                step_instance.number = 1
                step_instance.save()
                del request.session['form_step']
                return redirect('core:profile')

        return render(request, 'core:add_item.html', {'form': form, 'step': step})