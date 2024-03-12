from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse("category", kwargs={"pk": self.pk})
    


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    category = models.ManyToManyField(Category)
    description = models.TextField()
    products = models.TextField(blank=True)
    steps = models.TextField()
    make_time = models.DurationField(default=None)
    image = models.ImageField(upload_to='photo/', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


    def get_absolute_url(self):
        return reverse("recipe", kwargs={"id": self.pk})
    