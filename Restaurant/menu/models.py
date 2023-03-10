from django.db import models


class DietType(models.Model):
    DietTypeId = models.CharField(max_length=5)
    DietTypeName = models.CharField(max_length=30)

    def __str__(self):
        return self.DietTypeName

    class Meta:
        db_table = 'menu_diettype'


class MenuSection(models.Model):
    MenuSectionName = models.CharField(max_length=30)

    def __str__(self):
        return self.MenuSectionName

    class Meta:
        db_table = 'menu_menusection'


class Meal(models.Model):
    MealPicture = models.ImageField(
        upload_to="images/")
    MealName = models.CharField(
        max_length=30)
    MealIngredients = models.CharField(
        max_length=100)
    MealPrice = models.IntegerField(default=0)
    MealDietType = models.ForeignKey(
        DietType,  on_delete=models.CASCADE)
    MealSection = models.ForeignKey(
        MenuSection, on_delete=models.CASCADE)


class Menu(Meal):
    class Meta:
        proxy = True
