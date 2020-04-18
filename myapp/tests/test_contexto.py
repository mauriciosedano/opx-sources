from django.db import connection
from django.test import Client
from myapp.models import Contexto
from unittest import TestCase
from urllib.parse import urlencode
from .test_login import LoginTest
import json

class ContextoTest(TestCase):

    # Autenticación
    loginObj = LoginTest()
    token = loginObj.test()

    # Cabeceras generales
    headers = {
        'HTTP_AUTHORIZATION': 'Bearer ' + token
    }

    client = Client(**headers)

    # Listado
    def list(self, cantidad):

        response = self.client.get('/contextos/list/')

        cantidadContextos = len(json.loads(response.content))

        self.assertEqual(cantidadContextos, cantidad)

        if cantidad > 0:
            self.update()

    # Eliminación de los proyectos en la base de datos
    def clean(self):

        with connection.cursor() as cursor:
            cursor.execute('DELETE FROM v1.contextos;')

            self.store()

    # Almacenamiento
    def store(self):

            data = {
                'descripcion': 'Test',
            }

            response = self.client.post('/contextos/store/',
                                        urlencode(data),
                                        content_type='application/x-www-form-urlencoded')

            self.assertEqual(response.status_code, 201)

            self.list(1)

    # Actualización
    def update(self):

        # Obtener la decisión almacenada anteriormente
        contexto = Contexto.objects.get(descripcion='Test')

        data = {
            'descripcion': 'Test a',
        }

        response = self.client.post('/contextos/' + str(contexto.contextoid),
                                    urlencode(data),
                                    content_type='application/x-www-form-urlencoded')

        self.assertEqual(response.status_code, 200)

        self.delete()

    # Eliminación
    def delete(self):
        # Obtener el proyecto modificado anteriormente
        contexto = Contexto.objects.get(descripcion='Test a')

        response = self.client.delete('/contextos/delete/' + str(contexto.contextoid))

        self.assertEqual(response.status_code, 200)

        self.list(0)

    # Prueba
    def test(self):

        self.clean()