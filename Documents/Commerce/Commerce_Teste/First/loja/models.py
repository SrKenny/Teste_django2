from django.db import models


# Create your models here.

class Categories(models.Model):
    label = models.TextField()
    type = models.TextField()
    rank = models.IntegerField()
    image = models.ImageField()
    timestamp = models.DateTimeField()
    date_update = models.DateTimeField()
