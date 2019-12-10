from django.http.response import JsonResponse
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.forms.models import model_to_dict

from myapp.models import PlantillaEquipo, MiembroPlantilla
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend

from myapp.view.utilidades import usuarioAutenticado

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
            'code': 200,
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