from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.forms.models import model_to_dict
from django.http.response import JsonResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

from myapp.models import TipoProyecto

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def listadoTiposProyecto(request):

    tiposProyecto = TipoProyecto.objects.all().values()

    response = {
        'code': 200,
        'data': list(tiposProyecto),
        'status': 'success'
    }

    return JsonResponse(response, safe=False, status=response['code'])

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def almacenamientoTiposProyecto(request):

    try:
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')

        tipoProyecto = TipoProyecto(nombre=nombre, descripcion=descripcion)
        tipoProyecto.full_clean()
        tipoProyecto.save()

        response = {
            'code': 201,
            'data': model_to_dict(tipoProyecto),
            'status': 'success'
        }

    except ValidationError as e:
        response = {
            'code': 400,
            'errors': dict(e),
            'status': 'error'
        }

    return JsonResponse(response, safe=False, status=response['code'])

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def edicionTipoProyecto(request, tiproid):

    try:
        tipoProyecto = TipoProyecto.objects.get(pk=tiproid)

        tipoProyecto.nombre = request.POST.get('nombre')
        tipoProyecto.descripcion = request.POST.get('descripcion')

        tipoProyecto.full_clean()
        tipoProyecto.save()

        response = {
            'code': 200,
            'data': model_to_dict(tipoProyecto),
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
            'errors': dict(e),
            'status': 'error'
        }

    return JsonResponse(response, safe=False, status=response['code'])


@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def eliminarTipoProyecto(request, tiproid):

    try:
        tipoProyecto = TipoProyecto.objects.get(pk=tiproid)
        tipoProyecto.delete()

        response = {
            'code': 200,
            'status': 'success'
        }

    except ObjectDoesNotExist:
        response = {
            'code': 404,
            'status': 'error'
        }


    return JsonResponse(response, safe=False, status=response['code'])