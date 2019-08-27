from django.core import serializers
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.forms import model_to_dict
from django.http import HttpResponse, HttpResponseBadRequest
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from myapp import models

# ======================= usuarios ================================= 

def listadoUsuarios(request):

    users = models.Usuario.objects.all().values()
    # json_res = serializers.serialize('python', users)

    return JsonResponse(list(users), safe=False)

@csrf_exempt
def almacenarUsuario(request):

    useremail = request.POST.get('useremail')
    usertoken = request.POST.get('usertoken')
    userfullname = request.POST.get('userfullname')
    userpassword = request.POST.get('userpassword')
    rolid = request.POST.get('rolid')
    userleveltype = request.POST.get('userleveltype')
    userestado = request.POST.get('userestado')

    usuario = models.Usuario(useremail = useremail, usertoken = usertoken, userfullname = userfullname, userpassword = userpassword, rolid = rolid, userleveltype = userleveltype, userestado = userestado)

    try:
        usuario.full_clean()

        usuario.save()
        data = serializers.serialize('python', [usuario])
        return JsonResponse(data, safe = False, status = 201)

    except ValidationError as e:       
        return JsonResponse(dict(e), safe = True, status = 400)

@csrf_exempt
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
def actualizarUsuario(request, userid):
    
    try:
        usuario = models.Usuario.objects.get(pk = userid)

        usuario.useremail = request.POST.get('useremail')
        usuario.userpassword = request.POST.get('userpassword')
        usuario.rolid = request.POST.get('rolid')
        usuario.userleveltype = request.POST.get('userleveltype')
        usuario.userestado = request.POST.get('userestado')
        usuario.userfullname = request.POST.get('userfullname')
        usuario.usertoken = request.POST.get('usertoken')

        usuario.full_clean()

        usuario.save()

        return JsonResponse(serializers.serialize('python', [usuario]), safe = False)

    except ObjectDoesNotExist:
        return JsonResponse({'status': 'error'}, status = 404)

    except ValidationError as e:
        return JsonResponse({'status': 'error', 'errors': dict(e) }, status = 400)

def listadoUsuariosView(request):

    return render(request, 'proyectos/listado.html')

# ======================== Datos de Contexto =======================

def listadoDatosContexto(request):

    datosContexto = models.DatosContexto.objects.all().values()

    return JsonResponse(list(datosContexto), safe = False)

@csrf_exempt
def almacenarDatoContexto(request):

    hdxtag = request.POST.get('hdxtag')
    datavalor = request.POST.get('datavalor')
    datatipe = request.POST.get('datatipe')
    proyid = request.POST.get('proyid')

    datosContexto = models.DatosContexto(hdxtag = hdxtag, datavalor = datavalor, datatipe = datatipe, proyid = proyid)

    try:
        datosContexto.full_clean()

        datosContexto.save()
        data = serializers.serialize('python', [datosContexto])
        return JsonResponse(data, safe = False, status = 201)

    except ValidationError as e:
        return JsonResponse(dict(e), safe = True, status = 400)

@csrf_exempt
def eliminarDatoContexto(request, dataid):

    try:
        datoContexto = models.DatosContexto.objects.get(pk = dataid)

        datoContexto.delete()

        return JsonResponse({'status': 'success'})

    except ObjectDoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'El usuario no existe'}, safe = True, status = 404)

    except ValidationError:
        return JsonResponse({'status': 'error', 'message': 'Información inválida'}, safe = True, status = 400)

@csrf_exempt
def actualizarDatoContexto(request, dataid):
    try:
        datoContexto = models.DatosContexto.objects.get(pk=dataid)

        datoContexto.hdxtag = request.POST.get('hdxtag')
        datoContexto.datavalor = request.POST.get('datavalor')
        datoContexto.proyid = request.POST.get('proyid')
        datoContexto.datatipe = request.POST.get('datatipe')

        datoContexto.full_clean()

        datoContexto.save()

        return JsonResponse(serializers.serialize('python', [datoContexto]), safe=False)

    except ObjectDoesNotExist:
        return JsonResponse({'status': 'error'}, status=404)

    except ValidationError as e:
        return JsonResponse({'status': 'error', 'errors': dict(e)}, status=400)

# ======================== Decisiones =============================

def listadoDecisiones(request):

    decisiones = models.Decision.objects.all().values()

    return JsonResponse(list(decisiones), safe = False)

@csrf_exempt
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
def actualizarDecision(request, desiid):
    try:
        decision = models.Decision.objects.get(pk=desiid)

        decision.desidescripcion = request.POST.get('desidescripcion')
        decision.userid = request.POST.get('userid')

        decision.full_clean()

        decision.save()

        return JsonResponse(serializers.serialize('python', [decision]), safe=False)

    except ObjectDoesNotExist:
        return JsonResponse({'status': 'error'}, status=404)

    except ValidationError as e:
        return JsonResponse({'status': 'error', 'errors': dict(e)}, status=400)

# ========================== Decisiones Proyecto ==================

def listadoDecisionesProyecto(request):

    decisionesProyecto = models.DecisionProyecto.objects.all().values()

    return JsonResponse(list(decisionesProyecto), safe = False)

@csrf_exempt
def almacenarDecisionProyecto(request):

    proyid = request.POST.get('proyid')
    desiid = request.POST.get('desiid')

    decisionProyecto = models.DecisionProyecto(proyid = proyid, desiid = desiid)

    try:
        decisionProyecto.full_clean()

        decisionProyecto.save()
        data = serializers.serialize('python', [decisionProyecto])
        return JsonResponse(data, safe = False, status = 201)

    except ValidationError as e:
        return JsonResponse(dict(e), safe = True, status = 400)

@csrf_exempt
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

def listadoEquipos(request):

    equipos = models.Equipo.objects.all().values()

    return JsonResponse(list(equipos), safe = False)

@csrf_exempt
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

def listadoFuncionesRol(request):

    funcionesRol =  models.FuncionRol.objects.all().values()

    return JsonResponse(list(funcionesRol), safe = False)

@csrf_exempt
def almacenamientoFuncionRol(request):

    rolID = request.POST.get('rolid')
    actionID = request.POST.get('actionid')
    funcRolEstado = request.POST.get('funcrolestado')
    funcRolPermiso = request.POST.get('funcrolpermiso')

    funcionRol = models.FuncionRol(rolid = rolID, actionid = actionID, funcrolestado = funcRolEstado, funcrolpermiso = funcRolPermiso)

    try:
        funcionRol.full_clean()

        funcionRol.save()
        data = serializers.serialize('python', [funcionRol])
        return JsonResponse(data, safe = False, status = 201)

    except ValidationError as e:
        return JsonResponse(dict(e), safe = True, status = 400)

@csrf_exempt
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
def actualizarFuncionRol(request, funcrolid):

    try:
        funcionRol = models.FuncionRol.objects.get(pk=funcrolid)

        funcionRol.rolid = request.POST.get('rolid')
        funcionRol.actionid = request.POST.get('actionid')
        funcionRol.funcrolestado = request.POST.get('funcrolestado')
        funcionRol.funcrolpermiso = request.POST.get('funcrolpermiso')

        funcionRol.full_clean()

        funcionRol.save()

        return JsonResponse(serializers.serialize('python', [funcionRol]), safe=False)

    except ObjectDoesNotExist:
        return JsonResponse({'status': 'error'}, status=404)

    except ValidationError as e:

        return JsonResponse({'status': 'error', 'errors': dict(e)}, status=400)

# =============================== Instrumentos ===================

def listadoInstrumentos(request):

    instrumentos =  models.Instrumento.objects.all().values()

    return JsonResponse(list(instrumentos), safe = False)

@csrf_exempt
def almacenamientoInstrumento(request):

    instrIdExterno = request.POST.get('instridexterno')
    instrTipo = request.POST.get('instrtipo')

    instrumento = models.Instrumento(instridexterno = instrIdExterno, instrtipo = instrTipo)

    try:
        instrumento.full_clean()

        instrumento.save()
        data = serializers.serialize('python', [instrumento])
        return JsonResponse(data, safe = False, status = 201)

    except ValidationError as e:
        return JsonResponse(dict(e), safe = True, status = 400)

@csrf_exempt
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
def actualizarInstrumento(request, instrid):

    try:
        instrumento = models.Instrumento.objects.get(pk=instrid)

        instrumento.instridexterno = request.POST.get('instridexterno')
        instrumento.instrtipo = request.POST.get('instrtipo')

        instrumento.full_clean()

        instrumento.save()

        return JsonResponse(serializers.serialize('python', [instrumento]), safe=False)

    except ObjectDoesNotExist:
        return JsonResponse({'status': 'error'}, status=404)

    except ValidationError as e:

        return JsonResponse({'status': 'error', 'errors': dict(e)}, status=400)

# ============================= Proyectos ========================

def listadoProyectos(request):

    proyectos =  models.Proyecto.objects.all().values()

    return JsonResponse(list(proyectos), safe = False)

@csrf_exempt
def almacenamientoProyecto(request):

    proyNombre = request.POST.get('proynombre')
    proyDescripcion = request.POST.get('proydescripcion')
    proyIdExterno = request.POST.get('proyidexterno')
    proyFechaCreacion = request.POST.get('proyfechacreacion')
    proyFechaCierre = request.POST.get('proyfechacierre')
    proyEstado = request.POST.get('proyestado')    

    proyecto = models.Proyecto(proynombre = proyNombre, proydescripcion = proyDescripcion, proyidexterno = proyIdExterno, proyfechacreacion = proyFechaCreacion, proyfechacierre = proyFechaCierre, proyestado = proyEstado)

    try:
        proyecto.full_clean()

        proyecto.save()
        data = serializers.serialize('python', [proyecto])
        return JsonResponse(data, safe = False, status = 201)

    except ValidationError as e:
        return JsonResponse(dict(e), safe = True, status = 400)

@csrf_exempt
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
def actualizarProyecto(request, proyid):
    try:
        proyecto = models.Proyecto.objects.get(pk=proyid)

        proyecto.proynombre = request.POST.get('proynombre')
        proyecto.proydescripcion = request.POST.get('proydescripcion')
        proyecto.proyidexterno = request.POST.get('proyidexterno')
        proyecto.proyfechacreacion = request.POST.get('proyfechacreacion')
        proyecto.proyfechacierre = request.POST.get('proyfechacierre')
        proyecto.proyestado = request.POST.get('proyestado')

        proyecto.full_clean()

        proyecto.save()

        return JsonResponse(serializers.serialize('python', [proyecto]), safe=False)

    except ObjectDoesNotExist:
        return JsonResponse({'status': 'error'}, status=404)

    except ValidationError as e:

        return JsonResponse({'status': 'error', 'errors': dict(e)}, status=400)

# ============================ Roles =============================

def listadoRoles(request):

    roles =  models.Rol.objects.all().values()

    return JsonResponse(list(roles), safe = False)

@csrf_exempt
def almacenamientoRol(request):

    rolName = request.POST.get('rolname')
    rolDescripcion = request.POST.get('roldescripcion')   
    rolEstado = request.POST.get('rolestado')    

    rol = models.Rol(rolname = rolName, roldescripcion = rolDescripcion, rolestado = rolEstado)

    try:
        rol.full_clean()

        rol.save()
        data = serializers.serialize('python', [rol])
        return JsonResponse(data, safe = False, status = 201)

    except ValidationError as e:
        return JsonResponse(dict(e), safe = True, status = 400)

@csrf_exempt
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

# =========================== Tareas ==============================

def listadoTareas(request):

    tareas =  models.Tarea.objects.all().values()

    return JsonResponse(list(tareas), safe = False)

@csrf_exempt
def almacenamientoTarea(request):

    tareNombre = request.POST.get('tarenombre')
    tareTipo = request.POST.get('taretipo')
    tareRestricGeo = request.POST.get('tarerestricgeo')
    tareRestricCant = request.POST.get('tarerestriccant')
    tareRestricTime = request.POST.get('tarerestrictime')
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
def actualizarTarea(request, tareid):
    try:
        tarea = models.Tarea.objects.get(pk=tareid)

        tarea.tarenombre = request.POST.get('tarenombre')
        tarea.taretipo = request.POST.get('taretipo')
        tarea.tarerestricgeo = request.POST.get('tarerestricgeo')
        tarea.tarerestriccant = request.POST.get('tarerestriccant')
        tarea.tarerestrictime = request.POST.get('tarerestrictime')
        tarea.instrid = request.POST.get('instrid')
        tarea.proyid = request.POST.get('proyid')

        tarea.full_clean()

        tarea.save()

        return JsonResponse(serializers.serialize('python', [tarea]), safe=False)

    except ObjectDoesNotExist:
        return JsonResponse({'status': 'error'}, status=404)

    except ValidationError as e:
        return JsonResponse({'status': 'error', 'errors': dict(e)}, status=400)