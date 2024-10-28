from django.forms import ModelForm
from core.models import Item, ItemIngredient, ItemStep


class ItemForm(ModelForm):
     class Meta:
         model = Item
         fields = ['name', 'description', 'cooking_time', 'servings', 'image', 'category']


class ItemIngredientForm(ModelForm):
    class Meta:
        model = ItemIngredient
        fields = ['name', 'quantity']


class ItemStepForm(ModelForm):
    class Meta:
        model = ItemStep
        fields = ['name', 'image', 'text']