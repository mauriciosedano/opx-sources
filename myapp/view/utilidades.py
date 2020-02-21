from django.conf import settings
from django.http.response import JsonResponse
from django.shortcuts import render

from myapp import models

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

from rest_framework_simplejwt.backends import TokenBackend

#========================== Utilidades =============================

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

@api_view(['GET'])
@permission_classes((AllowAny,))
def listadoGeneros(request):

    generos = models.Genero.objects.all().values()

    data = {
        'code': 200,
        'generos': list(generos),
        'status': 'success'
    }

    return JsonResponse(data, status=data['code'], safe=False)

@api_view(['GET'])
@permission_classes((AllowAny,))
def listadoNivelesEducativos(request):

    nivelesEducativos = models.NivelEducativo.objects.all().values()

    data = {
        'code': 200,
        'nivelesEducativos': list(nivelesEducativos),
        'status': 'success'
    }

    return JsonResponse(data, status=data['code'], safe=False)

@api_view(['GET'])
@permission_classes((AllowAny,))
def listadoBarrios(request):

    barrios = models.Barrio.objects.all().values()

    data = {
        'code': 200,
        'barrios': list(barrios),
        'status': 'success'
    }

    return JsonResponse(data, status=data['code'], safe=False)

def usuarioAutenticado(request):

    # Decodificando el access token
    tokenBackend = TokenBackend(settings.SIMPLE_JWT['ALGORITHM'], settings.SIMPLE_JWT['SIGNING_KEY'],
                                settings.SIMPLE_JWT['VERIFYING_KEY'])
    tokenDecoded = tokenBackend.decode(request.META['HTTP_AUTHORIZATION'].split()[1], verify=True)
    # consultando el usuario
    user = models.Usuario.objects.get(pk=tokenDecoded['user_id'])

    return user

def obtenerParametroSistema(parametro):

    parametro = models.Parametro.objects.get(pk=parametro)

    if parametro is not None:
        response = parametro.paramvalor
    else:
        response = None

    return response

def notFoundPage(request, exception=None):
    return render(request, "error/404.html")

def serverErrorPage(request, exception=None):
    return render(request, "error/500.html")
