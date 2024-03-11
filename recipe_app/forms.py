from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Recipe


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password:', strip=False,
                                widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
                                help_text='''Your account password must meet the following requirements:
                                At least 12 characters, including uppercase and lowercase latin letters,
                                arabic numerals and other characters''')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class RecipeAddForm(forms.Form):
    recipe_name = forms.CharField(label='Recipe name:', max_length=100, required=True, widget=forms.TextInput(
        attrs={'class': 'recipe_name', 'placeholder': 'Input your recipe name'}))
    recipe_description = forms.CharField(label='Recipe description:', widget=forms.Textarea(
        attrs={'class': 'recipe_description', 'placeholder': 'Input your recipe description'}))
    recipe_cooking_steps = forms.CharField(label='Cooking order:', required=True, widget=forms.Textarea(
        attrs={'class': 'cooking_steps', 'placeholder': 'Input cooling steps.'}))
    recipe_cooking_time = forms.IntegerField(label='Cooking time (minutes):', min_value=1, required=True,
                                             widget=forms.NumberInput(attrs={
                                                 'class': 'cooking_time',
                                                 'placeholder': 'Input approximate time of cooking'}))
    recipe_category = forms.CharField(label='Recipe category:', widget=forms.TextInput(
        attrs={'class': 'recipe_category', 'placeholder': 'Input recipe category:'}))
    recipe_image = forms.ImageField(label='Recipe image:',
                                    widget=forms.ClearableFileInput(attrs={'class': 'recipe_image'}), )


class RecipeEditForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'cooking_steps', 'cooking_time', 'img', 'category']
        labels = {
            'name': 'Recipe name:',
            'description': 'Recipe description:',
            'cooking_steps': 'Cooking order:',
            'cooking_time': 'Cooking time (minutes):',
            'img': 'Recipe image:',
            'category': 'Recipe category:',
        }
