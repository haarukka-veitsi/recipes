from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Avatar')

    class Meta:
        db_table = 'User'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username


class ItemCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Item Category'
        verbose_name_plural = 'Item Categories'

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cooking_time = models.IntegerField(null=True, blank=True)
    servings = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='items_images', null=True, blank=True)
    author = models.ForeignKey(User,
                               models.SET_NULL,
                               blank=True, null=True)
    category = models.ForeignKey(ItemCategory,
                                 models.SET_NULL,
                                 blank=True, null=True)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return f'{self.name} ({self.id})'


class ItemIngredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item Ingredient'
        verbose_name_plural = 'Item Ingredients'


class ItemStep(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    text = models.TextField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item Step'
        verbose_name_plural = 'Item Steps'