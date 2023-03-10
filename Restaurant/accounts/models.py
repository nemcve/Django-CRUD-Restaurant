from django.db import models
from django.contrib.auth.models import User
from menu.models import DietType


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    UserAddress = models.CharField(max_length=30)
    UserNumber = models.IntegerField(unique=True)
    UserDietType = models.ForeignKey(
        DietType, verbose_name="Diet type", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
