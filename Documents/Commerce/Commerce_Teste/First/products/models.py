from django.conf import settings
from django.db import models
from django.utils import timezone



# Modelo Categoria

class Categories(models.Model):
    label = models.CharField(max_length=50, unique=True)
    type = models.CharField(max_length=50)
    rank = models.IntegerField()
    image = models.ImageField()
    timestamp = models.DateTimeField(default=timezone.now)
    date_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ('label',)

    # Função para apresentar o nome da categoria
    def __str__(self):
        return self.label


# Modelo Produto
class Products(models.Model):
    category = models.ForeignKey(Categories, related_name='categorias', null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=50, blank=False, default='')
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    price = models.FloatField(null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    date_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ('timestamp', 'name',)

    # Função para apresentar o products
    def __str__(self):
        return self.name



