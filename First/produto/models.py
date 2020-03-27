from django.conf import settings
from django.db import models
from django.utils import timezone


# Modelo Categoria

class Categories(models.Model):
    label = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    rank = models.IntegerField()
    image = models.ImageField()
    timestamp = models.DateTimeField(default=timezone.now)
    date_update = models.DateTimeField(blank=True, null=True)
    
    #Função para apresentar o nome da categoria
    def __str__(self):
        return self.label

