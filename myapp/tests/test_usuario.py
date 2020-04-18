from datetime import date
from django.db import connection
from django.test import Client
from myapp.models import Barrio, Genero, NivelEducativo, Rol, Usuario
from unittest import TestCase
from urllib.parse import urlencode
from .test_login import LoginTest
import json

class UsuarioTest(TestCase):

    # Autenticación
    loginObj = LoginTest()
    token = loginObj.test()

    # Cabeceras generales
    headers = {
        'HTTP_AUTHORIZATION': 'Bearer ' + token
    }

    client = Client(**headers)

    # Listado
    def list(self, cantidadBase, cantidadDeseada):

        response = self.client.get('/usuarios/list/')

        cantidadUsuarios = len(json.loads(response.content))

        self.assertEqual(cantidadUsuarios, cantidadDeseada)

        if cantidadDeseada > cantidadBase:
            self.update()

    # Eliminación de los proyectos en la base de datos
    def clean(self):

        with connection.cursor() as cursor:
            query = "DELETE FROM v1.usuarios " \
                    "WHERE rolid != '8945979e-8ca5-481e-92a2-219dd42ae9fc';"

            cursor.execute(query)

            self.store()

    # Almacenamiento
    def store(self):
            # Cantidad de usuarios
            cantidadUsuarios = len(Usuario.objects.all())

            # Obtener un rol del sistema
            rol = Rol.objects.first()

            # Obtener un sexo del sistema
            genero = Genero.objects.first()

            # Obtener un barrio del sistema
            barrio = Barrio.objects.first()

            # Obtener un nivel educativo del sistema
            nivelEducativo = NivelEducativo.objects.first()

            data = {
                'useremail': 'test@test.com',
                'password': 'test',
                'rolid': rol.rolid,
                'userfullname': 'test',
                'fecha_nacimiento': date.today(),
                'generoid': genero.generoid,
                'barrioid': barrio.barrioid,
                'nivel_educativo_id': nivelEducativo.nivelid,
                'telefono': '123456789'
            }

            response = self.client.post('/usuarios/store/',
                                        urlencode(data),
                                        content_type='application/x-www-form-urlencoded')

            self.assertEqual(response.status_code, 201)

            self.list(cantidadUsuarios, cantidadUsuarios + 1)

    # Actualización
    def update(self):

        # Obtener el usuario creado anteriormente
        usuario = Usuario.objects.get(useremail='test@test.com')

        # Obtener un rol del sistema
        rol = Rol.objects.first()

        # Obtener un sexo del sistema
        genero = Genero.objects.first()

        # Obtener un barrio del sistema
        barrio = Barrio.objects.first()

        # Obtener un nivel educativo del sistema
        nivelEducativo = NivelEducativo.objects.first()

        data = {
            'useremail': 'testa@test.com',
            'password': 'test',
            'rolid': rol.rolid,
            'userfullname': 'test',
            'fecha_nacimiento': date.today(),
            'generoid': genero.generoid,
            'barrioid': barrio.barrioid,
            'nivel_educativo_id': nivelEducativo.nivelid,
            'telefono': '123456789'
        }

        response = self.client.post('/usuarios/' + str(usuario.userid),
                                    urlencode(data),
                                    content_type='application/x-www-form-urlencoded')

        self.assertEqual(response.status_code, 200)

        self.delete()

    # Eliminación
    def delete(self):

        # Cantidad de Usuarios actual
        cantidadUsuarios = len(Usuario.objects.all())

        # Obtener el usuario creado anteriormente
        usuario = Usuario.objects.get(useremail='testa@test.com')

        response = self.client.delete('/usuarios/delete/' + str(usuario.userid))

        self.assertEqual(response.status_code, 200)

        self.list(cantidadUsuarios, cantidadUsuarios -1)

    # Prueba
    def test(self):

        self.clean()