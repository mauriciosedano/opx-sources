from django.http.response import JsonResponse
from myapp import models
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

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