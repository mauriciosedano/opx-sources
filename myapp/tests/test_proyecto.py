from datetime import date
from django.db import connection
from django.test import Client
from myapp.models import TipoProyecto, Proyecto
from unittest import TestCase
from urllib.parse import urlencode
from .test_login import LoginTest
import json

class ProyectoTest(TestCase):

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

        response = self.c.get('/proyectos/list/')

        cantidadProyectos = json.loads(response.content)['paginator']['total']

        self.assertEqual(cantidadProyectos, cantidad)

        if cantidad > 0:
            self.update()

    # Eliminación de los proyectos en la base de datos
    def clean(self):

        with connection.cursor() as cursor:
            cursor.execute('DELETE FROM v1.proyectos;')

            self.store()

    # Almacenamiento
    def store(self):
        # Obtener el primer tipo de proyecto al menos uno debe de existir
        tipoProyecto = TipoProyecto.objects.first()

        if tipoProyecto is not None:
            data = {
                'proynombre': 'Test',
                'proydescripcion': 'Test',
                'decisiones': [],
                'contextos': [],
                'delimitacionesGeograficas': [],
                'proyfechainicio': date.today(),
                'proyfechacierre': date.today(),
                'equipos': [],
                'tiproid': tipoProyecto.tiproid
            }

            response = self.c.post('/proyectos/store/', urlencode(data),
                                   content_type='application/x-www-form-urlencoded')

            self.assertEqual(response.status_code, 201)

            self.list(1)

    # Actualización
    def update(self):
        # Obtener el primer tipo de proyecto al menos uno debe de existir
        tipoProyecto = TipoProyecto.objects.first()

        # Obtener el proyecto almacenado anteriormente
        proyecto = Proyecto.objects.get(proynombre='Test')

        data = {
            'proynombre': 'Test a',
            'proydescripcion': 'Test a',
            'proyfechainicio': date.today(),
            'proyfechacierre': date.today(),
            'proyestado': 0,
            'tiproid': tipoProyecto.tiproid
        }

        response = self.c.post('/proyectos/' + str(proyecto.proyid), urlencode(data),
                               content_type='application/x-www-form-urlencoded')

        self.assertEqual(response.status_code, 200)

        self.delete()

    # Eliminación
    def delete(self):
        # Obtener el proyecto modificado anteriormente
        proyecto = Proyecto.objects.get(proynombre='Test a')

        response = self.c.delete('/proyectos/delete/' + str(proyecto.proyid) + '/')

        self.assertEqual(response.status_code, 200)

        self.list(0)

    # Prueba
    def test(self):

        self.clean()