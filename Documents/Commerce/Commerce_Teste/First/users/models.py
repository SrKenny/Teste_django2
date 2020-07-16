from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=150)
    password2 = models.CharField(max_length=150)

    def __str__(self):
        return self.username
