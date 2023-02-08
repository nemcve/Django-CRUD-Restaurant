from django.db import models


class DietType(models.Model):
    DietTypeId = models.CharField(max_length=5, null=False, blank=False)
    DietTypeName = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.DietTypeName

    class Meta:
        db_table = 'menu_diettype'


class MenuSection(models.Model):
    MenuSectionName = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.MenuSectionName

    class Meta:
        db_table = 'menu_menusection'


class Meal(models.Model):
    MealPicture = models.ImageField(
        upload_to="images/", blank=False, null=False)
    MealName = models.CharField(
        max_length=30, unique=True, blank=False, null=False)
    MealIngredients = models.CharField(
        max_length=100, blank=False, null=False)
    MealPrice = models.IntegerField(blank=False, null=False, default=0)
    MealDietType = models.ForeignKey(
        DietType, null=False, blank=False, on_delete=models.CASCADE)
    MealSection = models.ForeignKey(
        MenuSection, on_delete=models.CASCADE)


class Menu(Meal):
    class Meta:
        proxy = True
