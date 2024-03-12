from typing import Any
from django.core.management import BaseCommand
from recipes_book import models
from random import choice, randint
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone


class Command(BaseCommand):
    help = 'fill db'

    def handle(self, *args: Any, **options: Any) -> str | None:
        path = settings.BASE_DIR / 'recipes_book' / \
            'management' / 'commands' / 'recipe_md'
        with open(path / 'desc.md', 'r', encoding='UTF-8') as file:
            desc = file.read()
        with open(path / 'products.md', 'r', encoding='UTF-8') as file:
            products = file.read()
        with open(path / 'steps.md', 'r', encoding='UTF-8') as file:
            steps = file.read()
        with open(path / 'title.md', 'r', encoding='UTF-8') as file:
            title = file.read()
        categories = models.Category.objects.all()
        for _ in range(7):
            category=[]
            for _ in range(randint(1,2)):
                ctg = choice(categories)
                if ctg not in category:
                    category.append(ctg)
            recipe = models.Recipe(
                title=title,
                description=desc,
                products=products,
                steps=steps,
                make_time=timezone.timedelta(minutes=120),
                is_public=choice([True, False]),
                author=User.objects.filter(pk=1).first()
            )
            recipe.save()
            recipe.category.add(*category)
            recipe.save()
