from datetime import date
from django.db import connection
from django.test import Client
from myapp.models import Decision
from unittest import TestCase
from urllib.parse import urlencode
from .test_login import LoginTest
import json

class DecisionTest(TestCase):

    # Autenticación
    loginObj = LoginTest()
    token = loginObj.test()

    # Cabeceras generales
    headers = {
        'HTTP_AUTHORIZATION': 'Bearer ' + token
    }

    c = Client(**headers)

    # Listado
    def list(self, cantidad):

        response = self.c.get('/decisiones/list/')

        cantidadProyectos = len(json.loads(response.content))

        self.assertEqual(cantidadProyectos, cantidad)

        if cantidad > 0:
            self.update()

    # Eliminación de los proyectos en la base de datos
    def clean(self):

        with connection.cursor() as cursor:
            cursor.execute('DELETE FROM v1.decisiones;')

            self.store()

    # Almacenamiento
    def store(self):

            data = {
                'desidescripcion': 'Test',
            }

            response = self.c.post('/decisiones/store/',
                                   urlencode(data),
                                   content_type='application/x-www-form-urlencoded')

            self.assertEqual(response.status_code, 201)

            self.list(1)

    # Actualización
    def update(self):

        # Obtener la decisión almacenada anteriormente
        decision = Decision.objects.get(desidescripcion='Test')

        data = {
            'desidescripcion': 'Test a',
        }

        response = self.c.post('/decisiones/' + str(decision.desiid),
                               urlencode(data),
                               content_type='application/x-www-form-urlencoded')

        self.assertEqual(response.status_code, 200)

        self.delete()

    # Eliminación
    def delete(self):
        # Obtener el proyecto modificado anteriormente
        decision = Decision.objects.get(desidescripcion='Test a')

        response = self.c.delete('/decisiones/delete/' + str(decision.desiid) + '/')

        self.assertEqual(response.status_code, 200)

        self.list(0)

    # Prueba
    def test(self):

        self.clean()