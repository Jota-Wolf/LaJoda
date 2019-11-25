from django.test import TestCase
from .models import Cliente,Galeria
from django.contrib.auth.models import User
 
class ClienteTestCase(TestCase):

    def setUp(self):
        Cliente.objects.create(id='1',nombre ='joaquin',apellido ='lobos',rut = '18704536-3',telefono='5698734666',correo='lobos.joaquin@hotmail.com')
        Cliente.objects.create(id='2',nombre ='daniel',apellido ='gonzalez',rut = '20993213-1',telefono='5692213443',correo='gonzalez.daniel@gmail.com')

    def test_cliente_exists(self):
        cli1 = Cliente.objects.filter(nombre='joaquin').exists()
        cli2 = Cliente.objects.filter(id='2').exists()
        self.assertEqual(cli1,True)
        self.assertEqual(cli2,True)

class GaleriaTestCase(TestCase):

    def setUp(self):
        Galeria.objects.create(id='1',titulo ='kratos',imagen ='GoW-Ending.jpg',created_date ='2019-11-16 16:31:43',published_date='2019-11-16 16:31:43')

    def test_imagen_exists(self):
        existe = Galeria.objects.filter(titulo='kratos').exists()
        self.assertEqual(existe,True)

class UserTestCase(TestCase):

    def setUp(self):
        User.objects.create_user('jota','jota@gmail.com','jota1234')

    def test_user_exists(self):
        existe = User.objects.filter(username='jota').exists()
        self.assertEqual(existe,True)




