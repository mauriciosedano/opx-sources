from datetime import datetime
import json
import os
import http.client
from passlib.context import CryptContext

from myapp import models

from django.core import serializers
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db import connection
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

# ========================== Equipos ==============================

@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def equipoProyecto(request, proyid):

    try:

        if proyid is None:

            data = {
                'code': 400,
                'equipo': 'El proyecto no fue especificado',
                'status': 'error'
            }

        else:

            query = "select e.equid, u.userfullname, u.latitud, u.longitud, u.horaubicacion from v1.equipos as e inner join v1.usuarios as u on u.userid = e.userid where e.proyid = '" + proyid + "'"

            with connection.cursor() as cursor:
                cursor.execute(query)

                equipo = dictfetchall(cursor)

            data = {
                'code': 200,
                'equipo': equipo,
                'status': 'success'
            }

    except ValidationError as e:

        data = {
            'code': 400,
            'equipo': list(e),
            'status': 'success'
        }

    return JsonResponse(data, safe = False, status = data['code'])

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def almacenamientoEquipo(request):

    userid = request.POST.get('userid')
    proyid = request.POST.get('proyid')
    miembroEstado = 1
    #miembroEstado = request.POST.get('miembroestado')

    equipo = models.Equipo(userid = userid, proyid = proyid, miembroestado = miembroEstado)

    try:
        equipo.full_clean()

        equipo.save()

        data = {
            'code': 201,
            'integrante': serializers.serialize('python', [equipo])[0],
            'status': 'success'
        }

    except ValidationError as e:

        data = {
            'code': 400,
            'errors': dict(e),
            'status': 'error'
        }

    except IntegrityError as e:

        data = {
            'code': 500,
            'errors': str(e),
            'status': 'error'
        }

    return JsonResponse(data, safe = False, status = data['code'])

@csrf_exempt
@api_view(["DELETE"])
@permission_classes((IsAuthenticated,))
def eliminarEquipo(request, equid):

    try:
        equipo = models.Equipo.objects.get(pk = equid)

        equipo.delete()

        data = {
            'code': 200,
            'integrante': serializers.serialize('python', [equipo])[0],
            'status': 'success'
        }

    except ObjectDoesNotExist:

        data = {
            'code': 404,
            'message': 'El integrante no existe',
            'status': 'error'
        }

    except ValidationError as e:

        data = {
            'code': 400,
            'errors': tuple(e),
            'status': 'error'
        }

    return JsonResponse(data, safe = False, status = data['code'])

@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def actualizarEquipo(request, equid):
    try:
        equipo = models.Equipo.objects.get(pk=equid)
        proyectoID = request.POST.get('proyid')

        # Verificación de pertenencia de usuario a un proyecto
        verificacionIntegrante = models.Equipo.objects.filter(proyid__exact = proyectoID).filter(userid__exact = equipo.userid)

        if(len(verificacionIntegrante) == 0):

            equipo.proyid = proyectoID
            equipo.full_clean()
            equipo.save()

            response = {
                'code': 200,
                #'integrante': serializers.serialize('python', [equipo])[0],
                'status': 'success'
            }

        else:
            response = {
                'code': 403,
                'message': 'El usuario ya pertenece al proyecto especificado',
                'status': 'error'
            }

    except ObjectDoesNotExist:
        response = {
            'code': 404,
            'status': 'error'
        }

    except ValidationError as e:
        response = {
           'code': 400,
           'errors': dict(e),
           'status': 'error',
        }

    except IntegrityError as e:
        response = {
            'code': 500,
            'errors': str(e),
            'status': 'error'
        }

    return JsonResponse(response, status=response['code'])

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def usuariosDisponiblesProyecto(request, proyid):

    try:

        proyecto = models.Proyecto.objects.get(pk = proyid)

        # Busqueda de Usuarios
        search = request.GET.get('search')

        query = "select u.userid, u.userfullname from v1.usuarios u where u.rolid = '0be58d4e-6735-481a-8740-739a73c3be86' and u.userid not in (select e.userid from v1.equipos e where e.proyid = '" + proyid + "')"

        if search is not None:
            query += "and u.userfullname ~* '" + search + "'"

        with connection.cursor() as cursor:
            cursor.execute(query)

            usuarios = dictfetchall(cursor)

        data = {
            'code': 200,
            'usuarios': usuarios,
            'status': 'success'
        }

    except ObjectDoesNotExist:

        data = {
            'code': 404,
            'message': 'El proyecto no existe',
            'status': 'error'
        }

    except ValidationError as e:

        data = {
            'code': 400,
            'errors': tuple(e),
            'status': 'error'
        }

    return JsonResponse(data, safe = False, status = data['code'])

def equipoProyectoView(request, proyid):

    try:

        models.Proyecto.objects.get(pk = proyid)
        return render(request, "proyectos/equipo.html")

    except ObjectDoesNotExist:
        return HttpResponse("", status = 404)

    except ValidationError:
        return HttpResponse("", status = 400)