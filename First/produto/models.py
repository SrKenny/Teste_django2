from django.conf import settings
from django.db import models
from django.utils import timezone


# Modelo Categoria

class Categories(models.Model):  
    label = models.SlugField(max_length=50, unique=True, blank=True, null=True)
    type = models.CharField(max_length=50)
    rank = models.IntegerField()
    image = models.ImageField()
    timestamp = models.DateTimeField(default=timezone.now)
    date_update = models.DateTimeField(blank=True, null=True)
    categoria = []
    
    #Função para apresentar o nome da categoria     

    def __str__(self):
       return self.label

# Modelo Produto 
class Products(models.Model):
    category = Categories.label
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField()
    timestamp = models.DateTimeField(default=timezone.now)
    date_update = models.DateTimeField(blank=True, null=True)
     
    # Função para apresentar o produto
    def __str__(self):
       return self.name 



 