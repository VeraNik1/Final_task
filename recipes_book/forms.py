from django import forms
from recipes_book import models


class RecipeForm(forms.ModelForm):

    class Meta:
        model = models.Recipe
        fields = ("title", "category", "description", "products",
                  "steps", "make_time", "image", "is_public")
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', }),
            'category': forms.SelectMultiple(attrs={'class': 'form-control', }),
            'description': forms.Textarea(attrs={'class': 'form-control', }),
            'products': forms.Textarea(attrs={'class': 'form-control', }),
            'steps': forms.Textarea(attrs={'class': 'form-control', }),
            'make_time': forms.NumberInput(attrs={'class': 'form-control', }),
            'image': forms.FileInput(attrs={'class': 'form-control', }),
            'is_public': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'title': 'Название рецепта',
            'category': 'Выберите нужные категории',
            'description': 'Описание рецепта (в кодировке Markdown)',
            'products': 'Список продуктов (в кодировке Markdown)',
            'steps': 'Шаги приготовления (в кодировке Markdown)',
            'make_time': 'Время приготовления в минутах',
            'image': 'Фото готового блюда',
            'is_public': 'Опубликовать?',
        }


class DelConfirmForm(forms.Form):
    confirm = forms.BooleanField(
        label="Да, я подтвеждаю удаление",
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        })
    )
