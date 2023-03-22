from django.db import models


class Item(models.Model):
    title = models.CharField(
        'Name', max_length=64, help_text='Enter title item')


class Menu(models.Model):
    ...
