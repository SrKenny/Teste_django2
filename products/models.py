from django.conf import settings
from django.db import models
from django.contrib.postgres.fields import ArrayField


# Modelo Categoria

class Categories(models.Model):
    label = models.CharField(max_length=50, unique=True)
    type = models.CharField(max_length=50)
    rank = models.IntegerField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True, blank=True, null=True)

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
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    price = models.FloatField(null=True)
    related = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        ordering = ('timestamp', 'name',)

    # Função para apresentar o products
    def __str__(self):
        return self.name

    @property
    def related_indexing(self):
        """Filters for indexing.

        Used in Elasticsearch indexing.
        """
        return [self.related.all()]

