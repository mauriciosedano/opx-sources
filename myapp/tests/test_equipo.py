from django.db import connection
from django.test import Client
from myapp.models import PlantillaEquipo
from unittest import TestCase
from urllib.parse import urlencode
from .test_login import LoginTest
import json

class EquipoTest(TestCase):

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

        response = self.client.get('/plantillas-equipo/list/')

        cantidadPlantillasEquipo = len(json.loads(response.content)['data'])

        self.assertEqual(cantidadPlantillasEquipo, cantidad)

        if cantidad > 0:
            self.update()

    # Eliminación de los proyectos en la base de datos
    def clean(self):

        with connection.cursor() as cursor:
            cursor.execute('DELETE FROM v1.plantillas_equipo;')

            self.store()

    # Almacenamiento
    def store(self):

            data = {
                'descripcion': 'Test',
            }

            response = self.client.post('/plantillas-equipo/store/',
                                        urlencode(data),
                                        content_type='application/x-www-form-urlencoded')

            self.assertEqual(response.status_code, 201)

            self.list(1)

    # Actualización
    def update(self):

        # Obtener la decisión almacenada anteriormente
        equipo = PlantillaEquipo.objects.get(descripcion='Test')

        data = {
            'descripcion': 'Test a',
        }

        response = self.client.put('/plantillas-equipo/' + str(equipo.planid),
                                    urlencode(data),
                                    content_type='application/x-www-form-urlencoded')

        self.assertEqual(response.status_code, 200)

        self.delete()

    # Eliminación
    def delete(self):
        # Obtener el proyecto modificado anteriormente
        equipo = PlantillaEquipo.objects.get(descripcion='Test a')

        response = self.client.delete('/plantillas-equipo/' + str(equipo.planid) + '/delete/')

        self.assertEqual(response.status_code, 200)

        self.list(0)

    # Prueba
    def test(self):

        self.clean()