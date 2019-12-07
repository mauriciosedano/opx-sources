from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db import connection
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

from myapp.models import Proyecto, Rol, Usuario, Tarea, Instrumento, Encuesta
from myapp.view.utilidades import dictfetchall
from myapp.views import detalleFormularioKoboToolbox

# ==================== General ===================

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def usuariosXRol(request):

    roles = Rol.objects.all()

    data = {
        'roles': [],
        'cantidadUsuarios': []
    }

    for rol in roles:

        with connection.cursor() as cursor:

            query = "SELECT count(*) as cantidad from v1.usuarios where rolid = '" + str(rol.rolid) + "';"
            cursor.execute(query)

            data['roles'].append(rol.rolname)
            data['cantidadUsuarios'].append(dictfetchall(cursor)[0]['cantidad'])

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


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def proyectosTareas(request):

    proyectos = Proyecto.objects.all()

    data = []
    project = {}
    tareasProyecto = []
    progresoProyecto = 0

    for proyecto in proyectos:
        progresoProyecto = 0
        tareasProyecto = []

        project = {
            'id': proyecto.proyid,
            'name': proyecto.proynombre,
            'start': proyecto.proyfechainicio,
            'end': proyecto.proyfechacierre,
            'dependencies': ''
        }

        tareas = Tarea.objects.filter(proyid__exact=proyecto.proyid)

        for tarea in tareas:

            if tarea.taretipo == 1:

                task = {
                    'id': tarea.tareid,
                    'name': tarea.tarenombre,
                    'start': proyecto.proyfechainicio,
                    'end': proyecto.proyfechacierre,
                    'dependencies': proyecto.proyid
                }

                encuestas = Encuesta.objects.filter(tareid__exact=tarea.tareid)
                progreso = (len(encuestas) * 100) / tarea.tarerestriccant
                task['progress'] = progreso
                tareasProyecto.append(task)

                progresoProyecto = progresoProyecto + progreso


        if progresoProyecto > 0:
            progresoProyecto = (progresoProyecto * 100) / (len(tareas) * 100)

        project['progress'] = progresoProyecto

        data.append(project)
        data.extend(tareasProyecto)

    return JsonResponse(data, safe=False)

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

def estadisticasView(request):

    return render(request, "dashboard/estadisticas.html")


