from django.db import connection
from django.test import Client
from myapp.models import Rol
from unittest import TestCase
from urllib.parse import urlencode
from .test_login import LoginTest
import json

class RolTest(TestCase):

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

        response = self.client.get('/roles/list/')

        cantidadRoles = len(json.loads(response.content)['roles'])

        self.assertEqual(cantidadRoles, cantidad)

        if cantidad > 4:
            self.update()

    # Eliminación de los proyectos en la base de datos
    def clean(self):

        with connection.cursor() as cursor:
            query = "DELETE FROM v1.roles " \
                    "WHERE rolid != '628acd70-f86f-4449-af06-ab36144d9d6a' " \
                    "AND rolid != '53ad3141-56bb-4ee2-adcf-5664ba03ad65' " \
                    "AND rolid != '0be58d4e-6735-481a-8740-739a73c3be86' " \
                    "AND rolid != '8945979e-8ca5-481e-92a2-219dd42ae9fc';"

            cursor.execute(query)

            self.store()

    # Almacenamiento
    def store(self):

            data = {
                'rolname': 'Test',
                'roldescripcion': 'Test'
            }

            response = self.client.post('/roles/store/',
                                        urlencode(data),
                                        content_type='application/x-www-form-urlencoded')

            self.assertEqual(response.status_code, 201)

            self.list(5)

    # Actualización
    def update(self):

        # Obtener la decisión almacenada anteriormente
        rol = Rol.objects.get(rolname='Test')

        data = {
            'rolname': 'Test a',
            'roldescripcion': 'Test a'
        }

        response = self.client.post('/roles/' + str(rol.rolid),
                                    urlencode(data),
                                    content_type='application/x-www-form-urlencoded')

        self.assertEqual(response.status_code, 200)

        self.delete()

    # Eliminación
    def delete(self):
        # Obtener el proyecto modificado anteriormente
        rol = Rol.objects.get(rolname='Test a')

        response = self.client.delete('/roles/delete/' + str(rol.rolid))

        self.assertEqual(response.status_code, 200)

        self.list(4)

    # Prueba
    def test(self):

        self.clean()