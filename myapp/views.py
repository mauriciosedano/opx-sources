from datetime import datetime
import json
import os
import http.client
from urllib.parse import urlencode

from django.core import serializers
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db import connection
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
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

from myapp import models

#========================== Utilidades =============================

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

# ================================ Login ================================

def loginView(request):

    return render(request, "auth/login.html")

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):

    username = request.POST.get("username")
    password = request.POST.get("password")

    if username is None or password is None:

        data = {
           'status': 'error',
           'message': 'Por favor especifique usuario y contraseña',
           'code': 400
        }

    else:

        user = models.Usuario.objects.filter(useremail__exact = username).filter(password__exact = password)
        #user = authenticate(email=username, password=password)

        if len(user) == 0:

            data = {
                'status': 'error',
                'message': 'Usuario y/o contraseña incorrecta',
                'code': 404
            }

        else:
            refresh = RefreshToken.for_user(user[0])

            request.session['permisos'] = []

            permisos = models.FuncionRol.objects.filter(rolid__exact = user[0].rolid);

            for i in permisos:
                request.session['permisos'].append(str(i.accionid))

            print(request.session['permisos'])

            data = {
                'token': str(refresh.access_token),
                'user': {
                    'id': user[0].userid,
                    'name': user[0].userfullname,
                    'email': user[0].useremail
                },
                'code': 200
            }

            # token = Token.objects.get_or_create(user=user[0])

    return JsonResponse(data, status = data['code'])

# ======================= usuarios ================================= 

@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def listadoUsuarios(request):

    #users = models.Usuario.objects.all().values()
    # json_res = serializers.serialize('python', users)

    with connection.cursor() as cursor:
        cursor.execute("SELECT userid, userfullname, useremail, userestado, v1.usuarios.rolid, v1.roles.rolname FROM v1.usuarios INNER JOIN v1.roles ON v1.roles.rolid = v1.usuarios.rolid")
        columns = dictfetchall(cursor)

        return JsonResponse(columns, safe=False)

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def almacenarUsuario(request):

    useremail = request.POST.get('useremail')
    usertoken = request.POST.get('usertoken')
    userfullname = request.POST.get('userfullname')
    userpassword = request.POST.get('userpassword')
    rolid = request.POST.get('rolid')
    userleveltype = 1
    userestado = 1

    usuario = models.Usuario(useremail = useremail, usertoken = usertoken, userfullname = userfullname, password = userpassword, rolid = rolid, userleveltype = userleveltype, userestado = userestado)

    try:
        usuario.full_clean()

        usuario.save()
        data = serializers.serialize('python', [usuario])
        return JsonResponse(data, safe = False, status = 201)

    except ValidationError as e:       
        return JsonResponse(dict(e), safe = True, status = 400)

@csrf_exempt
@api_view(["DELETE"])
@permission_classes((IsAuthenticated,))
def eliminarUsuario(request, userid):

    try:
        usuario = models.Usuario.objects.get(userid = userid)

        usuario.delete()

        return JsonResponse({'status': 'success'})

    except ObjectDoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'El usuario no existe'}, safe = True, status = 404)

    except ValidationError:
        return JsonResponse({'status': 'error', 'message': 'Información inválida'}, safe = True, status = 400)

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def actualizarUsuario(request, userid):
    
    try:
        usuario = models.Usuario.objects.get(pk = userid)

        usuario.useremail = request.POST.get('useremail')
        usuario.password = request.POST.get('userpassword')
        usuario.rolid = request.POST.get('rolid')
        usuario.userfullname = request.POST.get('userfullname')


        usuario.full_clean()

        usuario.save()

        return JsonResponse(serializers.serialize('python', [usuario]), safe = False)

    except ObjectDoesNotExist:
        return JsonResponse({'status': 'error'}, status = 404)

    except ValidationError as e:
        return JsonResponse({'status': 'error', 'errors': dict(e) }, status = 400)

def listadoUsuariosView(request):

    return render(request, "usuarios/listado.html")

# ======================== Contextos ===============================

@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def listadoContextos(request):

    contextos = models.Contexto.objects.all().values()

    return JsonResponse(list(contextos), safe = False)

@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def almacenamientoContexto(request):

    descripcion = request.POST.get('descripcion');

    contexto = models.Contexto(descripcion=descripcion)

    try:
        contexto.full_clean()

        contexto.save()

        data = {
            'status': 'success',
            'contexto': serializers.serialize('python', [contexto])[0],
            'code': 201
        }
    except ValidationError as e:
        data = {
            'status': 'error',
            'errors': dict(e),
            'code': 400
        }

    return JsonResponse(data, safe = False, status = data['code'])

@api_view(["DELETE"])
@permission_classes((IsAuthenticated,))
def eliminarContexto(request, contextoid):

    try:
        contexto = models.Contexto.objects.get(pk = contextoid)

        contexto.delete()

        data = {
            'status': 'success',
            'code': 200
        }

    except ObjectDoesNotExist:

        data = {
            'status': 'error',
            'code': 404
        }

    except ValidationError:

        data = {
            'status': 'error',
            'message': 'Información inválida',
            'code': 400
        }

    return JsonResponse(data, status = data['code'])

@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def actualizarContexto(request, contextoid):

    descripcion = request.POST.get('descripcion')

    try:
        contexto = models.Contexto.objects.get(pk = contextoid)

        contexto.descripcion = descripcion

        contexto.full_clean()

        contexto.save()

        data = {
            'status': 'success',
            'contexto': serializers.serialize('python', [contexto])[0],
            'code': 200
        }

    except ObjectDoesNotExist:

        data = {
            'status': 'error',
            'code': 404
        }

    except ValidationError:

        data = {
            'status': 'error',
            'message': 'Información inválida',
            'code': 400
        }

    return JsonResponse(data, status = data['code'])

def listadoContextosView(request):

    return render(request, "contextos/listado.html")

# ======================== Datos de Contexto =======================

@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def listadoDatosContexto(request, contextoid):

    datosContexto = models.DatosContexto.objects.filter(contextoid__exact = contextoid).values()

    data = {
        'status': 'success',
        'datosContexto': list(datosContexto),
        'code': 200
    }

    return JsonResponse(data, safe = False, status = data['code'])

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def almacenarDatoContexto(request):

    hdxtag = request.POST.get('hdxtag')
    datavalor = " "
    datatipe = 1
    contextoid = request.POST.get('contextoid')

    datosContexto = models.DatosContexto(hdxtag = hdxtag, datavalor = datavalor, datatipe = datatipe, contextoid = contextoid)

    try:
        datosContexto.full_clean()

        if "file" in request.FILES.keys():
            file = request.FILES['file']

            if file.content_type != "text/csv" and file.content_type != "application/vnd.ms-excel":

                data = {
                   'status': 'error',
                   'errors':'El tipo de archivo no es permitido',
                    'code': 400
                }
                raise ValidationError(data)

        else:

            data = {
                'status': 'error',
                'errors': 'No se encontro ningun archivo',
                'code': 400
            }

            raise ValidationError(data)

        datosContexto.save()

        with open('/home/vagrant/code/opc-webpack/myapp/static/uploads/datoscontexto/' + str(datosContexto.dataid) + '.csv', 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        data = serializers.serialize('python', [datosContexto])
        return JsonResponse(data, safe = False, status = 201)

    except ValidationError as e:
        return JsonResponse(dict(e), safe = True, status = 400)

@csrf_exempt
@api_view(["DELETE"])
@permission_classes((IsAuthenticated,))
def eliminarDatoContexto(request, dataid):

    try:
        datoContexto = models.DatosContexto.objects.get(pk = dataid)

        datoContexto.delete()

        os.remove("/home/vagrant/code/opc-webpack/myapp/static/uploads/datoscontexto/" + dataid + ".csv")

        return JsonResponse({'status': 'success'})

    except ObjectDoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'El usuario no existe'}, safe = True, status = 404)

    except ValidationError:
        return JsonResponse({'status': 'error', 'message': 'Información inválida'}, safe = True, status = 400)

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def actualizarDatoContexto(request, dataid):
    try:
        datoContexto = models.DatosContexto.objects.get(pk=dataid)

        datoContexto.hdxtag = request.POST.get('hdxtag')
        #datoContexto.datavalor = request.POST.get('datavalor')
        #datoContexto.datatipe = request.POST.get('datatipe')

        datoContexto.full_clean()

        if "file" in request.FILES.keys():

            file = request.FILES['file']

            if file.content_type != "text/csv" and file.content_type != "application/vnd.ms-excel":

                data = {
                    'status': 'error',
                    'errors': 'El tipo de archivo no es permitido',
                    'code': 400
                }
                raise ValidationError(data)

            with open('/home/vagrant/code/opc-webpack/myapp/static/uploads/datoscontexto/' + str(
                    datoContexto.dataid) + '.csv', 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

        datoContexto.save()

        return JsonResponse(serializers.serialize('python', [datoContexto]), safe=False)

    except ObjectDoesNotExist:
        return JsonResponse({'status': 'error'}, status=404)

    except ValidationError as e:
        return JsonResponse({'status': 'error', 'errors': dict(e)}, status=400)

def listadoDatosContextoView(request, contextoid):

    try:
        contexto = models.Contexto.objects.get(pk = contextoid)

        return render(request, "contextos/datos-contexto.html", {'contexto': contexto})

    except ObjectDoesNotExist:
        code = 404

    except ValidationError:
        code = 400

    return HttpResponse("", status = code)



# ======================== Decisiones =============================

@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def listadoDecisiones(request):

    # decisiones = models.Decision.objects.all().values()
    #
    # return JsonResponse(list(decisiones), safe = False)

    with connection.cursor() as cursor:
        cursor.execute("select v1.decisiones.desiid, v1.decisiones.desidescripcion, v1.usuarios.userid, v1.usuarios.userfullname from v1.decisiones inner join v1.usuarios on v1.decisiones.userid = v1.usuarios.userid")

        columns = dictfetchall(cursor)

        return JsonResponse(columns, safe = False)

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def almacenarDecision(request):

    desidescripcion = request.POST.get('desidescripcion')
    userid = request.POST.get('userid')    

    decision = models.Decision(desidescripcion = desidescripcion, userid = userid)

    try:
        decision.full_clean()

        decision.save()
        data = serializers.serialize('python', [decision])
        return JsonResponse(data, safe = False, status = 201)

    except ValidationError as e:
        return JsonResponse(dict(e), safe = True, status = 400)

@csrf_exempt
@api_view(["DELETE"])
@permission_classes((IsAuthenticated,))
def eliminarDecision(request, desiid):

    try:
        decision = models.Decision.objects.get(pk = desiid)

        decision.delete()

        return JsonResponse({'status': 'success'})

    except ObjectDoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'El usuario no existe'}, safe = True, status = 404)

    except ValidationError:
        return JsonResponse({'status': 'error', 'message': 'Información inválida'}, safe = True, status = 400)

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def actualizarDecision(request, desiid):
    try:
        decision = models.Decision.objects.get(pk=desiid)

        decision.desidescripcion = request.POST.get('desidescripcion')
        # decision.userid = request.POST.get('userid')

        decision.full_clean()

        decision.save()

        return JsonResponse(serializers.serialize('python', [decision]), safe=False)

    except ObjectDoesNotExist:
        return JsonResponse({'status': 'error'}, status=404)

    except ValidationError as e:
        return JsonResponse({'status': 'error', 'errors': dict(e)}, status=400)

def listadoDecisionesView(request):

    return render(request, "decisiones/listado.html")


# ========================== Decisiones Proyecto ==================

@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def listadoDecisionesProyecto(request):

    decisionesProyecto = models.DecisionProyecto.objects.all().values()

    return JsonResponse(list(decisionesProyecto), safe = False)

def almacenarDecisionProyecto(proyecto, decisiones):

    try:
        for decision in decisiones:

            decisionProyecto = None

            decisionProyecto = models.DecisionProyecto(proyid = proyecto.proyid, desiid = decision)

            decisionProyecto.save()

        return True

    except ValidationError as e:
        return False

@csrf_exempt
@api_view(["DELETE"])
@permission_classes((IsAuthenticated,))
def eliminarDecisionProyecto(request, desproid):

    try:
        decisionProyecto = models.DecisionProyecto.objects.get(pk = desproid)

        decisionProyecto.delete()

        return JsonResponse({'status': 'success'})

    except ObjectDoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'El usuario no existe'}, safe = True, status = 404)

    except ValidationError:
        return JsonResponse({'status': 'error', 'message': 'Información inválida'}, safe = True, status = 400)

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def actualizarDecisionProyecto(request, desproid):
    try:
        decisionProyecto = models.DecisionProyecto.objects.get(pk=desproid)

        decisionProyecto.proyid = request.POST.get('proyid')
        decisionProyecto.desiid = request.POST.get('desiid')

        decisionProyecto.full_clean()

        decisionProyecto.save()

        return JsonResponse(serializers.serialize('python', [decisionProyecto]), safe=False)

    except ObjectDoesNotExist:
        return JsonResponse({'status': 'error'}, status=404)

    except ValidationError as e:
        return JsonResponse({'status': 'error', 'errors': dict(e)}, status=400)

# ========================== Equipos ==============================

@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def listadoEquipos(request):

    equipos = models.Equipo.objects.all().values()

    return JsonResponse(list(equipos), safe = False)

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def almacenamientoEquipo(request):

    userid = request.POST.get('userid')
    proyid = request.POST.get('proyid')
    miembroEstado = request.POST.get('miembroestado')

    equipo = models.Equipo(userid = userid, proyid = proyid, miembroestado = miembroEstado)

    try:
        equipo.full_clean()

        equipo.save()
        data = serializers.serialize('python', [equipo])
        return JsonResponse(data, safe = False, status = 201)

    except ValidationError as e:
        return JsonResponse(dict(e), safe = True, status = 400)

@csrf_exempt
@api_view(["DELETE"])
@permission_classes((IsAuthenticated,))
def eliminarEquipo(request, equid):

    try:
        equipo = models.Equipo.objects.get(pk = equid)

        equipo.delete()

        return JsonResponse({'status': 'success'})

    except ObjectDoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'El usuario no existe'}, safe = True, status = 404)

    except ValidationError:
        return JsonResponse({'status': 'error', 'message': 'Información inválida'}, safe = True, status = 400)

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def actualizarEquipo(request, equid):
    try:
        equipo = models.Equipo.objects.get(pk=equid)

        equipo.userid = request.POST.get('userid')
        equipo.proyid = request.POST.get('proyid')

        equipo.full_clean()

        equipo.save()

        return JsonResponse(serializers.serialize('python', [equipo]), safe=False)

    except ObjectDoesNotExist:
        return JsonResponse({'status': 'error'}, status=404)

    except ValidationError as e:
        return JsonResponse({'status': 'error', 'errors': dict(e)}, status=400)

# ========================= Funciones Rol =========================

@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def listadoAcciones(request):

    acciones = models.Accion.objects.all().values()

    return JsonResponse(list(acciones), safe = False)

@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def listadoFuncionesRol(request, rolid):

    with connection.cursor() as cursor:
        cursor.execute("select v1.funciones_rol.funcrolid, v1.acciones.nombre from v1.funciones_rol inner join v1.acciones on v1.funciones_rol.accionid = v1.acciones.accionid where v1.funciones_rol.rolid = %s", [rolid])

        columns = dictfetchall(cursor)

        return JsonResponse(columns, safe = False)

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def almacenamientoFuncionRol(request):

    rolID = request.POST.get('rolid')
    accionID = request.POST.get('accionid')
    funcRolEstado = 1
    funcRolPermiso = 1

    funcionRol = models.FuncionRol(rolid = rolID, accionid = accionID, funcrolestado = funcRolEstado, funcrolpermiso = funcRolPermiso)

    try:
        funcionRol.full_clean()

        funcionRol.save()
        data = serializers.serialize('python', [funcionRol])
        return JsonResponse(data, safe = False, status = 201)

    except ValidationError as e:
        return JsonResponse(dict(e), safe = True, status = 400)

@csrf_exempt
@api_view(["DELETE"])
@permission_classes((IsAuthenticated,))
def eliminarFuncionRol(request, funcrolid):

    try:
        funcionRol = models.FuncionRol.objects.get(pk = funcrolid)

        funcionRol.delete()

        return JsonResponse({'status': 'success'})

    except ObjectDoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'El usuario no existe'}, safe = True, status = 404)

    except ValidationError:
        return JsonResponse({'status': 'error', 'message': 'Información inválida'}, safe = True, status = 400)

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def actualizarFuncionRol(request, funcrolid):

    try:
        funcionRol = models.FuncionRol.objects.get(pk=funcrolid)

        #funcionRol.rolid = request.POST.get('rolid')
        funcionRol.actionid = request.POST.get('actionid')
        #funcionRol.funcrolestado = request.POST.get('funcrolestado')
        #funcionRol.funcrolpermiso = request.POST.get('funcrolpermiso')

        funcionRol.full_clean()

        funcionRol.save()

        return JsonResponse(serializers.serialize('python', [funcionRol]), safe=False)

    except ObjectDoesNotExist:
        return JsonResponse({'status': 'error'}, status=404)

    except ValidationError as e:

        return JsonResponse({'status': 'error', 'errors': dict(e)}, status=400)

# =============================== Instrumentos ===================

@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def listadoInstrumentos(request):

    instrumentos =  models.Instrumento.objects.all().values()

    return JsonResponse(list(instrumentos), safe = False)

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def almacenamientoInstrumento(request):

    instrIdExterno = "12345"
    instrTipo = request.POST.get('instrtipo')
    instrNombre = request.POST.get('instrnombre')
    instrDescripcion = request.POST.get('instrdescripcion')

    instrumento = models.Instrumento(instridexterno = instrIdExterno, instrtipo = instrTipo, instrnombre = instrNombre, instrdescripcion = instrDescripcion)

    try:
        instrumento.full_clean()

        instrumento.save()
        data = serializers.serialize('python', [instrumento])
        return JsonResponse(data, safe = False, status = 201)

    except ValidationError as e:
        return JsonResponse(dict(e), safe = True, status = 400)

@csrf_exempt
@api_view(["DELETE"])
@permission_classes((IsAuthenticated,))
def eliminarInstrumento(request, instrid):

    try:
        instrumento = models.Instrumento.objects.get(pk = instrid)

        instrumento.delete()

        return JsonResponse({'status': 'success'})

    except ObjectDoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'El usuario no existe'}, safe = True, status = 404)

    except ValidationError:
        return JsonResponse({'status': 'error', 'message': 'Información inválida'}, safe = True, status = 400)

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def actualizarInstrumento(request, instrid):

    try:
        instrumento = models.Instrumento.objects.get(pk=instrid)

        #instrumento.instridexterno = request.POST.get('instridexterno')
        instrumento.instrtipo = request.POST.get('instrtipo')
        instrumento.instrnombre = request.POST.get('instrnombre')
        instrumento.instrdescripcion = request.POST.get('instrdescripcion')

        instrumento.full_clean()

        instrumento.save()

        return JsonResponse(serializers.serialize('python', [instrumento]), safe=False)

    except ObjectDoesNotExist:
        return JsonResponse({'status': 'error'}, status=404)

    except ValidationError as e:

        return JsonResponse({'status': 'error', 'errors': dict(e)}, status=400)

def listadoInstrumentosView(request):

    return render(request, "instrumentos/listado.html")

def informacionInstrumentoView(request, id):

    try:
        instrumento = models.Instrumento.objects.get(pk = id)

        return render(request, "instrumentos/informacion-encuesta.html", {'instrumento': instrumento})

    except ObjectDoesNotExist:
        return HttpResponse("", status = 404)

    except ValidationError:
        return HttpResponse("", 400)

# ============================= Proyectos ========================

@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def listadoProyectos(request):

    proyectos =  models.Proyecto.objects.all().values()

    return JsonResponse(list(proyectos), safe = False)

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
    proyEstado = 0
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
        #proyecto.proyidexterno = request.POST.get('proyidexterno')
        #proyecto.proyfechacreacion = request.POST.get('proyfechacreacion')
        #proyecto.proyfechacierre = request.POST.get('proyfechacierre')
        #proyecto.proyestado = request.POST.get('proyestado')

        proyecto.full_clean()

        proyecto.save()

        return JsonResponse(serializers.serialize('python', [proyecto]), safe=False)

    except ObjectDoesNotExist:
        return JsonResponse({'status': 'error'}, status=404)

    except ValidationError as e:

        return JsonResponse({'status': 'error', 'errors': dict(e)}, status=400)


def listadoProyectosView(request):

    return render(request, 'proyectos/listado.html')

# ============================ Roles =============================

@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def listadoRoles(request):

    roles =  models.Rol.objects.all().values()

    return JsonResponse(list(roles), safe = False)

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def almacenamientoRol(request):

    rolName = request.POST.get('rolname')
    rolDescripcion = request.POST.get('roldescripcion')   
    rolEstado = 1

    rol = models.Rol(rolname = rolName, roldescripcion = rolDescripcion, rolestado = rolEstado)

    try:
        rol.full_clean()

        rol.save()
        data = serializers.serialize('python', [rol])
        return JsonResponse(data, safe = False, status = 201)

    except ValidationError as e:
        return JsonResponse(dict(e), safe = True, status = 400)

@csrf_exempt
@api_view(["DELETE"])
@permission_classes((IsAuthenticated,))
def eliminarRol(request, rolid):

    try:
        rol = models.Rol.objects.get(pk = rolid)

        rol.delete()

        return JsonResponse({'status': 'success'})

    except ObjectDoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'El usuario no existe'}, safe = True, status = 404)

    except ValidationError:
        return JsonResponse({'status': 'error', 'message': 'Información inválida'}, safe = True, status = 400)

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def actualizarRol(request, rolid):
    try:
        rol = models.Rol.objects.get(pk=rolid)

        rol.rolname = request.POST.get('rolname')
        rol.roldescripcion = request.POST.get('roldescripcion')        
        rol.rolestado = request.POST.get('rolestado')

        rol.full_clean()

        rol.save()

        return JsonResponse(serializers.serialize('python', [rol]), safe=False)

    except ObjectDoesNotExist:
        return JsonResponse({'status': 'error'}, status=404)

    except ValidationError as e:
        return JsonResponse({'status': 'error', 'errors': dict(e)}, status=400)

def listadoRolesView(request):

    return render(request, "roles/listado.html")

def permisosRolView(request, rolid):

    try:
        rol = models.Rol.objects.get(pk = rolid)

        return render(request, "roles/permisos.html", {'rol': rol})

    except ObjectDoesNotExist:
        return HttpResponse("", status = 404)

    except ValidationError:
        return HttpResponse("", status = 400)

# =========================== Tareas ==============================

@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def listadoTareas(request):

    #tareas =  models.Tarea.objects.all().values()

    #return JsonResponse(list(tareas), safe = False)

    query = "select v1.tareas.tareid, v1.tareas.tarenombre, v1.tareas.taretipo, v1.tareas.tarerestriccant, v1.instrumentos.instrid, v1.instrumentos.instrnombre, v1.proyectos.proyid, v1.proyectos.proynombre from v1.tareas inner join v1.proyectos on v1.tareas.proyid = v1.proyectos.proyid inner join v1.instrumentos on v1.tareas.instrid = v1.instrumentos.instrid"

    with connection.cursor() as cursor:
        cursor.execute(query)

        columns = dictfetchall(cursor)

        return JsonResponse(columns, safe = False)

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

    tarea = models.Tarea(tarenombre = tareNombre, taretipo = tareTipo, tarerestricgeo = tareRestricGeo, tarerestriccant = tareRestricCant, tarerestrictime = tareRestricTime, instrid = instrID, proyid = proyID)

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

# ================= Kobo Toolbox ========================

def informacionInstrumento(request, id):

    try:
        instrumento = models.Instrumento.objects.get(pk = id)

        if instrumento.instrtipo == 1:

            informacion = informacionFormularioKoboToolbox(instrumento.instridexterno)
            print(type(informacion))

            if(isinstance(informacion, dict)):

                data = {
                    'status': 'success',
                    'code': 200,
                    'info': informacion
                }

            else:

                data = {
                    'status': 'error',
                    'code': 500
                }

        else:

            data = {
                'status': 'error',
                'code': 404
            }

    except ObjectDoesNotExist:

        data = {
            'status': 'error',
            'code': 404
        }

    except ValidationError:

        data = {
            'status': 'error',
            'code': 400
        }

    return JsonResponse(data, status = data['code'])


def informacionFormularioKoboToolbox(id):

    headers = {'Authorization': 'Token 9e65dbdf164fbcee05f739d5e2d269e908760d8d'}

    client = http.client.HTTPConnection("kf.oim-opc.pre", 80, timeout = 10)

    client.request('GET', '/assets/' + id + '/submissions/', '{}', headers)

    response = client.getresponse()

    if(response.status != 200):

        data = False

    else:

        info = json.loads(response.read())

        # ============== Obteniendo campos del formulario====================

        client = http.client.HTTPConnection("kf.oim-opc.pre", 80, timeout=10)
        client.request('GET', '/assets/?format=json', '', headers)
        response = client.getresponse()

        if (response.status == 200):

            formulariosKoboToolbox = json.loads(response.read())['results']

            for i in formulariosKoboToolbox:

                if (i['uid'] == id):

                    campos = i['summary']['labels']
                    break

            data = {
                'campos': campos,
                'info': info
            }

        else:

            data = False

    client.close()

    return data

@csrf_exempt
def implementarFormularioKoboToolbox(request, id):

    try:

        instrumento = models.Instrumento.objects.get(pk = id)

        headers = {
            'Authorization': 'Token 9e65dbdf164fbcee05f739d5e2d269e908760d8d',
            'Content-Type': 'application/json'
        }

        payload = {'active': True}

        client = http.client.HTTPConnection("kf.oim-opc.pre", 80, timeout = 10)

        client.request('POST', '/assets/' + instrumento.instridexterno + '/deployment/', json.dumps(payload), headers)

        response = client.getresponse()

        if response.status != 200:

            data = {
                'status': 'error',
                'code': 500
            }

        else:

            data = {
                'status': 'success',
                'code': 200
            }

    except ObjectDoesNotExist:

        data = {
            'status': 'error',
            'code': 404
        }

    except ValidationError:

        data = {
            'status': 'error',
            'code': 400
        }

    return JsonResponse(data, status = data['code'])


def verificarImplementaciónFormulario(request, id):

    try:
        instrumento = models.Instrumento.objects.get(pk = id)

        headers = {
            'Authorization': 'Token 9e65dbdf164fbcee05f739d5e2d269e908760d8d',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'
        }

        client = http.client.HTTPConnection("kf.oim-opc.pre", 80, timeout=10)
        client.request('GET', '/assets/?format=json', '', headers)
        response = client.getresponse()

        if(response.status == 200):

            formulariosKoboToolbox = json.loads(response.read())['results']

            for i in formulariosKoboToolbox:

                if(i['uid'] == instrumento.instridexterno):

                    if(i['has_deployment']):

                        data = {
                            'code': 200,
                            'status': 'success',
                            'implementacion': True
                        }

                    else:

                        data = {
                            'code': 200,
                            'status': 'success',
                            'implementacion': False
                        }

                    break

                else:

                    data = {
                        'code': 404,
                        'status': 'error'
                    }

        else:

            data = {
                'code': 500,
                'status': 'error'
            }

    except ObjectDoesNotExist:

        data = {
            'status': 'success',
            'code': 404
        }

    except ValidationError:

        data = {
            'status': 'error',
            'code': 400
        }

    return JsonResponse(data, status = data['code'])