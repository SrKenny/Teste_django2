from django.test import RequestFactory, TestCase
from django.contrib.auth.models import AnonymousUser
from .models import Products, Categories
from .views import ProductsViewSet, CategoriesViewSet

# Create your tests here.
class CategoriesTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.category = Categories.objects.create(label='Games', type='Eletronics', rank='1', image='none')


    def test_categories(self):
       request = self.factory.get('/produto/category')
       #Usuário anonimo
       request.user = AnonymousUser()
       #Teste da cotegoria





#class ProdutoTestCase(TestCase):
 #   def setUp(self):
  #      Products.objects.create(title='Console', name='Nintendo Switch', description='Video game para a criançada.', image='none')
   #     Products.objects.create(title='Console', name='PlayStation 4', description='Video game robusto.', image='none')









