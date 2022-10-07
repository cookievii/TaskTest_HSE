from core.models import UUIDModel
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser, UUIDModel):
    username = models.CharField("Имя", max_length=150, unique=True)
    password = models.CharField("Пароль", max_length=150)

    REQUIRED_FIELDS = ["password"]

    def __str__(self):
        return self.username
