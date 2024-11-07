from django import forms
from core.models import Item, ItemIngredient, ItemStep, User


class ItemForm(forms.ModelForm):
     class Meta:
         model = Item
         fields = ['name', 'description', 'cooking_time', 'servings', 'image', 'category']


class ItemIngredientForm(forms.ModelForm):
    class Meta:
        model = ItemIngredient
        fields = ['name', 'quantity']


class ItemStepForm(forms.ModelForm):
    class Meta:
        model = ItemStep
        fields = ['name', 'image', 'text']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'image']
