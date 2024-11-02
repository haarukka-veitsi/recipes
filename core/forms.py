from django import forms
from core.models import Item, ItemIngredient, ItemStep, UserImage


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


class UserImageForm(forms.ModelForm):
    class Meta:
        model = UserImage
        fields = ['image']
