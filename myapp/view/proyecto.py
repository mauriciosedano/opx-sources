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

# ============================= Proyectos ========================

@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def listadoProyectos(request):

    try:

        search = request.GET.get('search')
        page = request.GET.get('page')

        # Consultando proyectos
        if search is None:

            proyectos =  models.Proyecto.objects.all()

        else:
            proyectos = models.Proyecto.objects.filter(proynombre__icontains = search)

        # Especificando orden
        proyectos = proyectos.order_by('-proyfechacreacion')

        # Paginación
        paginator = Paginator(proyectos, 10)

        # Validación de página
        if page is None:
            page = 1

        #Petición de página
        proyectos = paginator.page(page).object_list.values()

        data = {
            'code': 200,
            'paginator': {
                'currentPage': int(page),
                'perPage': paginator.per_page,
                'lastPage': paginator.num_pages,
                'total': paginator.count
            },
            'proyectos': list(proyectos),
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

    #return HttpResponse(request.POST.get('proynombre'))

    proyNombre = request.POST.get('proynombre')
    proyDescripcion = request.POST.get('proydescripcion')
    proyIdExterno = 12345
    proyFechaCreacion = datetime.today()
    proyFechaCierre = request.POST.get('proyfechacierre')
    proyEstado = 1
    decisiones = json.loads(request.POST.get('decisiones'))
    contextos = json.loads(request.POST.get('contextos'))

    proyecto = models.Proyecto(proynombre = proyNombre, proydescripcion = proyDescripcion, proyidexterno = proyIdExterno, proyfechacreacion = proyFechaCreacion, proyfechacierre = proyFechaCierre, proyestado = proyEstado)

    try:
        proyecto.full_clean()

        proyecto.save()

        almacenarDecisionProyecto(proyecto, decisiones)
        almacenarContextosProyecto(proyecto, contextos)

        data = serializers.serialize('python', [proyecto])
        return JsonResponse(data, safe = False, status = 201)

    except ValidationError as e:
        return JsonResponse(dict(e), safe = True, status = 400)

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