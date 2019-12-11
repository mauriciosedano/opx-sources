from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import connection
from django.forms.models import model_to_dict
from django.http.response import JsonResponse
from django.shortcuts import render

from myapp.models import PlantillaEquipo, MiembroPlantilla
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend

from myapp.view.utilidades import usuarioAutenticado, dictfetchall

# ============================== Plantillas de Equipo ================================

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def listadoPlantillas(request):

    user = usuarioAutenticado(request)

    if(str(user.rolid) == '628acd70-f86f-4449-af06-ab36144d9d6a'):

        plantillas = PlantillaEquipo.objects.all().values()

        response = {
            'code': 200,
            'data': list(plantillas),
            'status': 'success'
        }

    else:
        response = {
            'code': 403,
            'message': 'Usuario no permitido',
            'status': 'error'
        }

    return JsonResponse(response, safe=False, status=response['code'])

@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def eliminarPlantilla(request, planid):

    try:
        plantilla = PlantillaEquipo.objects.get(pk=planid)
        plantilla.delete()

        response = {
            'code': 200,
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

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def crearPlantilla(request):

    try:

        user = usuarioAutenticado(request)
        descripcion = request.POST.get('descripcion')

        plantilla = PlantillaEquipo(descripcion=descripcion, userid=user.userid)
        plantilla.full_clean()
        plantilla.save()

        response = {
            'code': 201,
            'data': model_to_dict(plantilla),
            'status': 'success'
        }

    except ValidationError as e:

        response = {
            'code': 400,
            'errors': dict(e),
            'status': 'success'
        }


    return JsonResponse(response, safe=False, status=response['code'])

@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def edicionPlantilla(request, planid):

    try:
        plantilla = PlantillaEquipo.objects.get(pk=planid)

        plantilla.descripcion = request.POST.get('descripcion')

        response = {
            'code': 200,
            'data': model_to_dict(plantilla),
            'status': 'success'
        }

        plantilla.full_clean()
        plantilla.save()

    except ObjectDoesNotExist:
        response = {
            'code': 404,
            'status': 'error'
        }

    except ValidationError as e:
        response = {
            'code': 400,
            'errors': dict(e),
            'status': 'error'
        }

    return JsonResponse(response, safe=False, status=response['code'])


# ============================ Miembros de plantilla =====================================

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def miembrosPlantilla(request, planid):

    try:
        #miembrosPlantilla = MiembroPlantilla.objects.filter(planid__exact=planid).values()
        with connection.cursor() as cursor:
            query = "select mp.miplid, u.userfullname from v1.miembros_plantilla mp inner join v1.usuarios u on u.userid = mp.userid " \
                    "where mp.planid = '" + planid + "'"

            cursor.execute(query)

            miembrosPlantilla = dictfetchall(cursor)

        response = {
            'code': 200,
            'data': miembrosPlantilla,
            'status': 'success'
        }

    except ValidationError as e:

        response = {
            'code': 400,
            'errors': list(e)[0],
            'status': 'error'
        }

    return JsonResponse(response, safe=False, status=response['code'])

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def agregarMiembro(request, planid):

    try:

        plantillaEquipo = PlantillaEquipo.objects.get(pk=planid)

        userid = request.POST.get('userid')

        cantidadUsuarios = MiembroPlantilla.objects.filter(userid__exact=userid) \
                                            .filter(planid__exact=planid)

        if len(cantidadUsuarios) == 0:

            miembroPlantilla = MiembroPlantilla(userid=userid, planid=planid)
            miembroPlantilla.full_clean()
            miembroPlantilla.save()

            response = {
                'code': 201,
                'data': model_to_dict(miembroPlantilla),
                'status': 'success'
            }

        else:
            response = {
                'code': 403,
                'message': 'El usuario ya hace parte de la plantilla',
                'status': 'error'
            }

    except ObjectDoesNotExist:
        response = {
            'code': 404,
            'status': 'error'
        }

    except ValidationError as e:

        try:
            errors = dict(e)
        except ValueError:
            errors = list(e)[0]

        response = {
            'code': 400,
            'errors': errors,
            'status': 'error'
        }

    return JsonResponse(response, safe=False, status=response['code'])

@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def eliminarMiembro(request, miplid):

    try:
        miembroPlantilla = MiembroPlantilla.objects.get(pk=miplid)

        miembroPlantilla.delete()

        response = {
            'code': 200,
            'status': 'success'
        }

    except ObjectDoesNotExist:
        response = {
            'code': 404,
            'status': 'error'
        }

    except ValidationError as e:

        response = {
            'code': 400,
            'errors': list(e)[0],
            'status': 'error'
        }

    return JsonResponse(response, safe=False, status=response['code'])

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def miembrosDisponibles(request, planid):

    try:

        plantilla = PlantillaEquipo.objects.get(pk = planid)

        # Busqueda de Usuarios
        search = request.GET.get('search')

        query = "select u.userid, u.userfullname from v1.usuarios u where (u.rolid = '0be58d4e-6735-481a-8740-739a73c3be86' or u.rolid = '53ad3141-56bb-4ee2-adcf-5664ba03ad65') and u.userid not in (select mp.userid from v1.miembros_plantilla mp where mp.planid = '" + planid + "')"

        if search is not None:
            query += "and u.userfullname ~* '" + search + "'"

        with connection.cursor() as cursor:
            cursor.execute(query)

            usuarios = dictfetchall(cursor)

        response = {
            'code': 200,
            'usuarios': usuarios,
            'status': 'success'
        }

    except ObjectDoesNotExist:

        response = {
            'code': 404,
            'message': 'La plantilla no existe',
            'status': 'error'
        }

    except ValidationError as e:

        response = {
            'code': 400,
            'errors': list(e)[0],
            'status': 'error'
        }

    return JsonResponse(response, safe = False, status = response['code'])

def plantillasView(request):

    return render(request, "proyectos/gestion-plantillas.html")