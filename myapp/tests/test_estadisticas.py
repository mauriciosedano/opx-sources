from django.db import connection
from django.test import Client
from myapp.models import PlantillaEquipo
from unittest import TestCase
from urllib.parse import urlencode
from .test_login import LoginTest
import json

class EstadisticaTest(TestCase):

    # Autenticación
    loginObj = LoginTest()
    token = loginObj.test()

    # Cabeceras generales
    headers = {
        'HTTP_AUTHORIZATION': 'Bearer ' + token
    }

    client = Client(**headers)

    def datosGenerales(self):

        response = self.client.get('/estadisticas/datos-generales/')

        self.assertEqual(response.status_code, 200)

    def usuariosXRol(self):

        response = self.client.get('estadisticas/usuarios-x-rol/')

        self.assertEqual(response.status_code, 200)

    def usuariosXSexo(self):

        response = self.client.get('/estadisticas/usuarios-x-genero/')

        self.assertEqual(response.status_code, 200)

    def usuariosXNivelEducativo(self):

        response = self.client.get('/estadisticas/usuarios-x-nivel-educativo/')

        self.assertEqual(response.status_code, 200)

    def usuariosXBarrio(self):

        response = self.client.get('/estadisticas/usuarios-x-barrio/')

        self.assertEqual(response.status_code, 200)

    def ranking(self):

        response = self.client.get('/estadisticas/ranking/')

        self.assertEqual(response.status_code, 200)

    # Prueba
    def test(self):

        self.datosGenerales()
        self.usuariosXRol()
        self.usuariosXSexo()
        self.usuariosXNivelEducativo()
        self.usuariosXBarrio()
        self.ranking()