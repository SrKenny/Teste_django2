from django.conf import settings
from django.db import models
from django.utils import timezone


# Modelo Categoria

<<<<<<< Updated upstream:First/produto/models.py
class Categories(models.Model):  
=======
class Categories(models.Model):
>>>>>>> Stashed changes:Documents/Commerce/Commerce_Teste/First/produto/models.py
    label = models.SlugField(max_length=50, unique=True, blank=True, null=True)
    type = models.CharField(max_length=50)
    rank = models.IntegerField()
    image = models.ImageField()
    timestamp = models.DateTimeField(default=timezone.now)
    date_update = models.DateTimeField(blank=True, null=True)
<<<<<<< Updated upstream:First/produto/models.py
    categoria = []
=======

>>>>>>> Stashed changes:Documents/Commerce/Commerce_Teste/First/produto/models.py
    
    #Função para apresentar o nome da categoria     

    def __str__(self):
       return self.label

# Modelo Produto 
class Products(models.Model):
<<<<<<< Updated upstream:First/produto/models.py
    category = Categories.label
=======
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
>>>>>>> Stashed changes:Documents/Commerce/Commerce_Teste/First/produto/models.py
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField()
    timestamp = models.DateTimeField(default=timezone.now)
    date_update = models.DateTimeField(blank=True, null=True)
     
    # Função para apresentar o produto
    def __str__(self):
       return self.name 



 