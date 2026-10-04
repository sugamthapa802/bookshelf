from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    bio=models.CharField(blank=True,default="")
    avatar=models.URLField(blank=True,default="")

    def __str__(self):
        return self.username
