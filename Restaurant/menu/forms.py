from django import forms
from .models import Meal


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = "__all__"
        labels = {
            "MealPicture": "Meal picture ",
            "MealName": "Meal name ",
            "MealIngredients": "Meal ingredients ",
            "MealPrice": "Meal price ",
            "MealDietType": "Meal type ",
            "MealSection": "Meal menu section ",
        }
