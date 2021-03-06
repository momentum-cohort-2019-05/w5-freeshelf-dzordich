# pylint: disable=mixed-line-endings

from datetime import date
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.

class Favorites(models.Model):
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    book = models.ForeignKey('Book', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.owner}'


class Book(models.Model):
    title = models.CharField(max_length=100, help_text="Enter name of book")
    date = models.DateField(default=date.today)
    author = models.CharField(max_length=25, help_text="Enter name of author")
    url = models.URLField()
    description = models.CharField(max_length=500, help_text="Enter brief description for book")

    category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.SET_NULL)


    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.pk)])

    def __str__(self):
        return f'{self.title}'


    class Meta:
        ordering = ['-date']


class Category(models.Model):
    name = models.CharField(max_length=20, help_text="Title of this category of books")
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Comment(models.Model):

    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)
    content = models.CharField(max_length=256, help_text="Enter comment.")
    commenter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.content)

    class Meta:
        ordering = ['date']
