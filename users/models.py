from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone


class CustomUser(AbstractUser):
    name = models.CharField(max_length=150,  blank=True, null=True)
    email = models.EmailField()
    password = models.CharField(max_length=150)
    password2 = models.CharField(max_length=150)
    favorite = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.username

    @property
    def favorites_indexing(self):
        """Favorites for indexing.

        Used in Elasticsearch indexing.
        """
        return [self.favorite.all()]
