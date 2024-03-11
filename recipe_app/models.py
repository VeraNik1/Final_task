from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Category')

    class Meta:
        verbose_name = 'Categories'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='', blank=True)
    cooking_steps = models.TextField(default='', blank=True)
    cooking_time = models.IntegerField()
    img = models.ImageField(
        upload_to='photos/%Y/%m/%d/',
        blank=True,
        default=None,
        null=True,
        verbose_name='Image'
    )
    author = models.ForeignKey(Author, on_delete=models.SET_DEFAULT, default='Author unknown')
    category = models.ManyToManyField(
        'Category',
        blank=True,
        related_name='category_recipes',
        verbose_name='Category'
    )

    time_create = models.DateTimeField(auto_now_add=True, verbose_name='added_at')

    class Meta:
        verbose_name = 'Recipes'
        verbose_name_plural = 'Recipes'
        ordering = ['-time_create']
