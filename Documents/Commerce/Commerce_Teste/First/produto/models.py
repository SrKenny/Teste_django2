from django.conf import settings
from django.db import models
from django.utils import timezone


# Modelo Categoria

class Categories(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    label = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    rank = models.IntegerField()
    image = models.ImageField()
    timestamp = models.DateTimeField(default=timezone.now)
    date_update = models.DateTimeField(blank=True, null=True)
    
    #Função para apresentar o nome da categoria
    def categoria(self):
       self.label = print(self)
       self.save()

    def __str__(self):
       return self.label

# Modelo Produto 
class Products(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.DateTimeField()
    timestamp = models.DateTimeField(default=timezone.now)
    date_update = models.DateTimeField(blank=True, null=True)
     
    # Função para apresentar o produto
    def product(self):
       self.title = print(self)



 