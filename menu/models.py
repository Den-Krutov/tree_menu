from django.db import models


class BaseModel(models.Model):
    title = models.CharField('Title', max_length=64, help_text='Enter title')
    slug = models.SlugField('Slug', max_length=64, help_text='Enter URL page')

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.title


class Menu(BaseModel):
    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'


class Item(BaseModel):
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name='items')
    parent = models.ForeignKey(
        'self', blank=True, null=True, on_delete=models.CASCADE,
        related_name='childrens')

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
