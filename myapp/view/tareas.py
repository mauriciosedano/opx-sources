from datetime import datetime
import json
import os
import http.client
from passlib.context import CryptContext

from myapp import models

from django.core import serializers
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.core.paginator import(
    Paginator,
    EmptyPage
)
from django.db import (connection, transaction)
from django.db.utils import IntegrityError
from django.http import HttpResponse, HttpResponseBadRequest
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

from myapp.view.utilidades import dictfetchall

# =========================== Tareas ==============================

@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def listadoTareas(request):

    try:

        # Obtener página validación de la misma
        page = request.GET.get('page')

        if(page is None):
            page = 1

        # Obtener Búsqueda y validación de la misma
        search = request.GET.get('search')

        if search is None:
            query = "select v1.tareas.tareid, v1.tareas.tarenombre, v1.tareas.taretipo, v1.tareas.tarerestriccant, v1.instrumentos.instrid, v1.instrumentos.instrnombre, v1.proyectos.proyid, v1.proyectos.proynombre from v1.tareas inner join v1.proyectos on v1.tareas.proyid = v1.proyectos.proyid inner join v1.instrumentos on v1.tareas.instrid = v1.instrumentos.instrid"
        else:
            query = "select v1.tareas.tareid, v1.tareas.tarenombre, v1.tareas.taretipo, v1.tareas.tarerestriccant, v1.instrumentos.instrid, v1.instrumentos.instrnombre, v1.proyectos.proyid, v1.proyectos.proynombre from v1.tareas inner join v1.proyectos on v1.tareas.proyid = v1.proyectos.proyid inner join v1.instrumentos on v1.tareas.instrid = v1.instrumentos.instrid where v1.tareas.tarenombre ~* '" + search + "'"


        print(query)
        with connection.cursor() as cursor:
            cursor.execute(query)

            # formatear respuesta de base de datos
            tareas = dictfetchall(cursor)

            # Obtener Página
            paginator = Paginator(tareas, 10)

            # Obtener lista de tareas
            tareas = paginator.page(page).object_list

            data = {
                'code': 200,
                'paginator': {
                    'currentPage': page,
                    'perPage': paginator.per_page,
                    'lastPage': paginator.num_pages,
                    'total': paginator.count
                },
                'tareas': tareas,
                'status': 'success'
            }

    except EmptyPage:

        data = {
            'code': 400,
            'message': 'Página inexistente',
            'status': 'error'
        }

    return JsonResponse(data, safe = False, status = data['code'])

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def almacenamientoTarea(request):

    tareNombre = request.POST.get('tarenombre')
    tareTipo = request.POST.get('taretipo')
    tareRestricGeo = "{}"
    tareRestricCant = request.POST.get('tarerestriccant')
    tareRestricTime = "{}"
    instrID = request.POST.get('instrid')
    proyID = request.POST.get('proyid')
    dimensionid = request.POST.get('dimensionid')
    geojson_subconjunto = request.POST.get('geojson_subconjunto')

    tarea = models.Tarea(tarenombre = tareNombre, taretipo = tareTipo, tarerestricgeo = tareRestricGeo, tarerestriccant = tareRestricCant, tarerestrictime = tareRestricTime, instrid = instrID, proyid = proyID, dimensionid = dimensionid, geojson_subconjunto = geojson_subconjunto)

    try:
        tarea.full_clean()

        tarea.save()
        data = serializers.serialize('python', [tarea])
        return JsonResponse(data, safe = False, status = 201)

    except ValidationError as e:
        return JsonResponse(dict(e), safe = True, status = 400)

@csrf_exempt
@api_view(["DELETE"])
@permission_classes((IsAuthenticated,))
def eliminarTarea(request, tareid):

    try:
        tarea = models.Tarea.objects.get(pk = tareid)

        tarea.delete()

        return JsonResponse({'status': 'success'})

    except ObjectDoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'El usuario no existe'}, safe = True, status = 404)

    except ValidationError:
        return JsonResponse({'status': 'error', 'message': 'Información inválida'}, safe = True, status = 400)

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def actualizarTarea(request, tareid):
    try:
        tarea = models.Tarea.objects.get(pk=tareid)

        tarea.tarenombre = request.POST.get('tarenombre')
        tarea.taretipo = request.POST.get('taretipo')
        tarea.tarerestricgeo = "{}"
        tarea.tarerestriccant = request.POST.get('tarerestriccant')
        tarea.tarerestrictime = "{}"
        tarea.instrid = request.POST.get('instrid')
        tarea.proyid = request.POST.get('proyid')

        tarea.full_clean()

        tarea.save()

        return JsonResponse(serializers.serialize('python', [tarea]), safe=False)

    except ObjectDoesNotExist:
        return JsonResponse({'status': 'error'}, status=404)

    except ValidationError as e:
        return JsonResponse({'status': 'error', 'errors': dict(e)}, status=400)

def listadoTareasView(request):

    return render(request, 'tareas/listado.html')