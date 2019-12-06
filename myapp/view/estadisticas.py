from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db import connection
from django.http.response import JsonResponse, HttpResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

from myapp.models import Proyecto, Rol, Usuario
from myapp.view.utilidades import dictfetchall

# ==================== General ===================

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def usuariosXRol(request):

    roles = Rol.objects.all()

    data = []

    for rol in roles:

        with connection.cursor() as cursor:

            query = "SELECT count(*) as cantidad from v1.usuarios where rolid = '" + str(rol.rolid) + "';"
            cursor.execute(query)

            data.append({
                'rol': rol.rolname,
                'cantidad': dictfetchall(cursor)[0]['cantidad']
            })

    response = {
         'code': 200,
         'data': data,
         'status': 'success'
    }

    return JsonResponse(response, safe=False, status=response['code'])

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def cantidadUsuarios(request):

    with connection.cursor() as cursor:

        query = "SELECT count(*) as cantidad from v1.usuarios;"
        cursor.execute(query)

        response = {
            'code': 200,
            'data': dictfetchall(cursor)[0]['cantidad'],
            'status': 'success'
        }

    return JsonResponse(response, safe=False, status=response['code'])

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def ranking(request):

    usuarios = Usuario.objects.order_by('-puntaje').values()

    response = {
        'code': 200,
        'data': list(usuarios)[0:3],
        'status': 'success'
    }

    return JsonResponse(response, safe=False, status=response['code'])


# ==================== Especifico ============================

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def tareasXTipo(request, proyid):

    try:

        proyecto = Proyecto.objects.get(pk=proyid)

        tiposTarea = [
            {
                'label': 'Encuesta',
                'value': '1'
            },
            {
                'label': 'Cartografia',
                'value': '2'
            }
        ]

        data = {}

        for tipo in tiposTarea:

            with connection.cursor() as cursor:

                 query = "SELECT count(*) as cantidad from v1.tareas where taretipo = {} and proyid = '{}'" \
                         .format(tipo['value'], proyid)

                 cursor.execute(query)

                 data[tipo['label']] = dictfetchall(cursor)[0]['cantidad']

        response = {
             'code': 200,
             'data': data,
             'status': 'success'
        }

    except ObjectDoesNotExist:
        response = {
            'code': 404,
            'status': 'error'
        }

    except ValidationError:
        response = {
            'code': 400,
            'status': 'error'
        }

    return JsonResponse(response, safe=False, status=response['code'])

def tareasXEstado(request, proyid):

    try:

        proyecto = Proyecto.objects.get(pk=proyid)

        tiposTarea = [
            {
                'label': 'En progreso',
                'value': '0'
            },
            {
                'label': 'Terminada',
                'value': '1'
            },
            {
                'label': 'Validada',
                'value': '2'
            }
        ]

        data = []

        for tipo in tiposTarea:

            with connection.cursor() as cursor:

                 query = "SELECT count(*) as cantidad from v1.tareas where tareestado = {} and proyid = '{}'" \
                         .format(tipo['value'], proyid)

                 cursor.execute(query)

                 data.append({
                    'tipo': tipo['label'],
                    'cantidad': dictfetchall(cursor)[0]['cantidad']
                 })

        response = {
            'code': 200,
            'data': data,
            'status': 'success'
        }

    except ObjectDoesNotExist:
        response = {
            'code': 404,
            'status': 'error'
        }

    except ValidationError:
        response = {
            'code': 400,
            'status': 'error'
        }

    return JsonResponse(response, safe=False, status=response['code'])
