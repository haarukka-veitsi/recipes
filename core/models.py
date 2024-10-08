from django.db import models


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
    ingredients = models.TextField()
    cooking_steps = models.TextField()
    cooking_time = models.IntegerField(null=True, blank=True)
    servings = models.IntegerField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

