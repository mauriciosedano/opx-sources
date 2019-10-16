from datetime import datetime
import json
import os
import http.client
from passlib.context import CryptContext

from myapp import models

from django.conf import settings
from django.core import serializers
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.core.paginator import(
    Paginator,
    EmptyPage
)
from django.db import connection
from django.db.utils import IntegrityError
from django.http import HttpResponse, HttpResponseBadRequest
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

from myapp.view.utilidades import dictfetchall

# ============================= Proyectos ========================

@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def listadoProyectos(request):

    #Decodificando el access token
    tokenBackend = TokenBackend(settings.SIMPLE_JWT['ALGORITHM'], settings.SIMPLE_JWT['SIGNING_KEY'], settings.SIMPLE_JWT['VERIFYING_KEY'])
    tokenDecoded = tokenBackend.decode(request.META['HTTP_AUTHORIZATION'].split()[1], verify = True)

    try:
        #consultando el usuario
        user = models.Usuario.objects.get(pk = tokenDecoded['user_id'])

        search = request.GET.get('search')
        page = request.GET.get('page')

        # ============================ Consultando proyectos ====================================

        #Consulta de proyectos para super administrador
        if str(user.rolid) == '8945979e-8ca5-481e-92a2-219dd42ae9fc':
            proyectos = models.Proyecto.objects.all()

        # Consulta de proyectos para proyectista
        elif str(user.rolid) == '628acd70-f86f-4449-af06-ab36144d9d6a':
            proyectos = models.Proyecto.objects.filter(proypropietario__exact = user.userid)

        # Consulta de proyectos para voluntarios
        elif str(user.rolid) == '0be58d4e-6735-481a-8740-739a73c3be86':

            proyectosAsignados = models.Equipo.objects.filter(userid__exact = user.userid)
            proyectosAsignadosID = []

            for p in proyectosAsignados:
                proyectosAsignadosID.append(p.proyid)

            proyectos = models.Proyecto.objects.filter(pk__in = proyectosAsignadosID)


        else:
            proyectos = models.Proyecto.objects.filter(proynombre = 'qwerty')

        # Busqueda de proyectos
        if search:
            proyectos = proyectos.filter(proynombre__icontains = search)

        # Especificando orden
        proyectos = proyectos.order_by('-proyfechacreacion')

        # convirtiendo a lista de diccionarios
        proyectos = list(proyectos.values())

        listadoProyectos = []
        for p in proyectos:
            p['proyectista'] = models.Usuario.objects.get(pk = p['proypropietario']).userfullname
            listadoProyectos.append(p)

        # Paginación
        paginator = Paginator(listadoProyectos, 5)

        # Validación de página
        if page is None:
            page = 1

        #Petición de página
        proyectos = paginator.page(page).object_list

        data = {
            'code': 200,
            'paginator': {
                'currentPage': int(page),
                'perPage': paginator.per_page,
                'lastPage': paginator.num_pages,
                'total': paginator.count
            },
            'proyectos': proyectos,
            'status': 'success',
        }

    except EmptyPage:

        data = {
            'code': 404,
            'message': 'Página inexistente',
            'status': 'error'
        }

    return JsonResponse(data, safe = False, status = data['code'])

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def almacenamientoProyecto(request):

    # Decodificando el access token
    tokenBackend = TokenBackend(settings.SIMPLE_JWT['ALGORITHM'], settings.SIMPLE_JWT['SIGNING_KEY'], settings.SIMPLE_JWT['VERIFYING_KEY'])
    tokenDecoded = tokenBackend.decode(request.META['HTTP_AUTHORIZATION'].split()[1], verify=True)

    proyNombre = request.POST.get('proynombre')
    proyDescripcion = request.POST.get('proydescripcion')
    proyIdExterno = 12345
    proyFechaCreacion = datetime.today()
    proyFechaCierre = request.POST.get('proyfechacierre')
    proyEstado = 1
    decisiones = json.loads(request.POST.get('decisiones'))
    contextos = json.loads(request.POST.get('contextos'))
    propietario = tokenDecoded['user_id']

    proyecto = models.Proyecto(proynombre = proyNombre, proydescripcion = proyDescripcion, proyidexterno = proyIdExterno, proyfechacreacion = proyFechaCreacion, proyfechacierre = proyFechaCierre, proyestado = proyEstado, proypropietario = propietario)

    try:
        proyecto.full_clean()

        proyecto.save()

        almacenarDecisionProyecto(proyecto, decisiones)
        almacenarContextosProyecto(proyecto, contextos)

        data = serializers.serialize('python', [proyecto])[0]

        data = {
            'code': 201,
            'proyecto': data,
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
            'message': str(e),
            'status': 'success'
        }

    return JsonResponse(data, safe = False, status = data['code'])

def almacenarDecisionProyecto(proyecto, decisiones):

    try:
        for decision in decisiones:

            decisionProyecto = None

            decisionProyecto = models.DecisionProyecto(proyid = proyecto.proyid, desiid = decision)

            decisionProyecto.save()

        return True

    except ValidationError as e:
        return False

def almacenarContextosProyecto(proyecto, contextos):

    try:
        for contexto in contextos:

            contextoProyecto = models.ContextoProyecto(proyid = proyecto.proyid, contextoid = contexto)

            contextoProyecto.save()

            del contextoProyecto

        return True

    except ValidationError as e:
        return False

@csrf_exempt
@api_view(["DELETE"])
@permission_classes((IsAuthenticated,))
def eliminarProyecto(request, proyid):

    try:
        proyecto = models.Proyecto.objects.get(pk = proyid)

        proyecto.delete()

        return JsonResponse({'status': 'success'})

    except ObjectDoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'El usuario no existe'}, safe = True, status = 404)

    except ValidationError:
        return JsonResponse({'status': 'error', 'message': 'Información inválida'}, safe = True, status = 400)

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def actualizarProyecto(request, proyid):
    try:
        proyecto = models.Proyecto.objects.get(pk=proyid)

        proyecto.proynombre = request.POST.get('proynombre')
        proyecto.proydescripcion = request.POST.get('proydescripcion')
        decisiones = json.loads(request.POST.get('decisiones'))
        contextos = json.loads(request.POST.get('contextos'))

        proyecto.full_clean()

        proyecto.save()

        # ================ Actualizacion de decisiones ===============================
        decisionesProyecto = models.DecisionProyecto.objects.filter(proyid__exact = proyecto.proyid)

        if decisionesProyecto.exists():

            for decisionProyecto in decisionesProyecto:

                decisionProyecto.delete()

        if len(decisiones) > 0:

            for decision in decisiones:

                decisionProyecto = models.DecisionProyecto(proyid = proyecto.proyid, desiid = decision)
                decisionProyecto.save()

        # ============== Actualización de contextos ================================

        contextosProyecto = models.ContextoProyecto.objects.filter(proyid__exact = proyecto.proyid)

        if contextosProyecto.exists():

            for contextoProyecto in contextosProyecto:

                contextoProyecto.delete()

        if len(contextos) > 0:

            for contexto in contextos:

                contextoProyecto = models.ContextoProyecto(proyid = proyecto.proyid, contextoid = contexto)
                contextoProyecto.save()

        return JsonResponse(serializers.serialize('python', [proyecto]), safe=False)

    except ObjectDoesNotExist:
        return JsonResponse({'status': 'error'}, status=404)

    except ValidationError as e:

        return JsonResponse({'status': 'error', 'errors': dict(e)}, status=400)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def detalleProyecto(request, proyid):

    try:

        proyecto = models.Proyecto.objects.get(pk = proyid)

        # Obtención de Tareas
        tareas = models.Tarea.objects.filter(proyid__exact = proyid)

        data = {
            'code': 200,
            'detail':{
              'proyecto': serializers.serialize('python', [proyecto])[0],
              'tareas': serializers.serialize('python', tareas)
            },
            'status': 'success'
        }

    except ObjectDoesNotExist:

        data = {
            'code': 404,
            'status': "error",
        }

    except ValidationError:

        data = {
            'code': 400,
            'status': 'error'
        }

    return JsonResponse(data, status = data['code'], safe = False)


def listadoProyectosView(request):

    return render(request, 'proyectos/listado.html')