from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    bonuses = models.FloatField(default=0)

    def __str__(self):
        return self.username

    def __repr__(self):
        return self.username + " "
