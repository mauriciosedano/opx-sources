from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
import uuid

class MyUserManager(BaseUserManager):
    use_in_migrations = True

##
# @brief Modelo de usuario
#
class Usuario(AbstractBaseUser):
    userid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    useremail = models.EmailField(max_length = 255, unique=True)
    password = models.CharField(max_length = 255)
    usertoken = models.CharField(max_length = 255, null = True, blank = True)
    userfullname = models.CharField(max_length = 255)
    rolid = models.UUIDField()
    userleveltype = models.IntegerField()
    userestado = models.IntegerField()
    fecha_nacimiento = models.DateField()
    generoid = models.UUIDField()
    barrioid = models.IntegerField()
    nivel_educativo_id = models.UUIDField()
    telefono = models.CharField(max_length=20)
    latitud = models.CharField(blank=True, null=True, max_length=30)
    longitud = models.CharField(blank=True, null=True, max_length=30)
    horaubicacion = models.CharField(blank=True, null=True, max_length=100)
    puntaje = models.IntegerField(null=True, blank=True, default=0)

    objects = MyUserManager()

    USERNAME_FIELD = "useremail"

    class Meta:
        db_table = '"v1"."usuarios"'

##
# @brief Modelo de Contextos
#
class Contexto(models.Model):

    contextoid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    descripcion = models.CharField(max_length = 1000)

    class Meta:
        db_table = '"v1"."contextos"'

##
# @brief Modelo de Datos de Contexto
#
class DatosContexto(models.Model):

    dataid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    hdxtag = models.CharField(max_length = 100)
    datavalor = models.CharField(max_length = 100)
    datatipe = models.CharField(max_length=100)
    contextoid = models.UUIDField()
    descripcion = models.CharField(max_length=500)
    geojson = models.CharField(max_length=3000)
    fecha = models.DateField(null=True, blank=True)
    hora = models.TimeField(null=True, blank=True)

    class Meta:
        db_table = '"v1"."datos_contexto"'

##
# @brief Modelo de Contextos Proyecto
#
class ContextoProyecto(models.Model):

    contproyid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    proyid = models.UUIDField()
    contextoid = models.UUIDField()

    class Meta:
        db_table = '"v1"."contextos_proyecto"'

##
# @brief Modelo de Decisiones
#
class Decision(models.Model):
    desiid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    desidescripcion = models.CharField(max_length = 1000)
    userid = models.UUIDField()

    class Meta:
        db_table = '"v1"."decisiones"'

##
# @brief Modelo de Decisiones Proyecto
#
class DecisionProyecto(models.Model):
    desproid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    proyid = models.UUIDField()
    desiid = models.UUIDField()

    class Meta:
        db_table = '"v1"."decisiones_proyecto"'

##
# @brief Modelo de Equipos
#
class Equipo(models.Model):
    equid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    userid = models.UUIDField()
    proyid = models.UUIDField()
    miembroestado = models.IntegerField(default=1)

    class Meta:
        db_table = '"v1"."equipos"'

##
# @brief Modelo de Permisos del Sistema
#
class Accion(models.Model):
    accionid = models.UUIDField(primary_key= True, default = uuid.uuid4(), editable = False)
    nombre = models.CharField(max_length = 255)
    descripcion = models.CharField(max_length = 1000)

    class Meta:
        db_table = '"v1"."acciones"'

##
# @brief Modelo de permisos para los roles
#
class FuncionRol(models.Model):
    funcrolid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    rolid = models.UUIDField()
    accionid = models.CharField(max_length = 255)
    funcrolestado = models.IntegerField()
    funcrolpermiso = models.IntegerField()

    class Meta:
        db_table = '"v1"."funciones_rol"'

##
# @brief Modelo de instrumentos
#
class Instrumento(models.Model):
    instrid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    instridexterno = models.CharField(max_length = 255)
    instrtipo = models.IntegerField()
    instrnombre = models.CharField(max_length = 255)
    instrdescripcion = models.CharField(max_length = 3000, null = True, blank = True)
    geojson = models.CharField(max_length=1000, null = True, blank=True)

    class Meta:
        db_table = '"v1"."instrumentos"'

##
# @brief Modelo de Proyectos
#
class Proyecto(models.Model):
    proyid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    proynombre = models.CharField(max_length = 255)
    proydescripcion = models.TextField()
    proyidexterno = models.CharField(max_length = 255)
    proyfechacreacion = models.CharField(max_length=100)
    proyfechacierre = models.DateField(null=True, blank=True)
    proyestado = models.IntegerField()
    proypropietario = models.UUIDField()
    proyfechainicio = models.DateField(null=True, blank=True)
    tiproid = models.UUIDField()

    class Meta:
        db_table = '"v1"."proyectos"'

##
# @brief Modelo de Roles del sistema
#
class Rol(models.Model):
    rolid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    rolname = models.CharField(max_length=50)
    roldescripcion = models.CharField(max_length = 255)
    rolestado = models.IntegerField()

    class Meta:
        db_table = '"v1"."roles"'

##
# @brief Modelo de Tareas
#
class Tarea(models.Model):

    tareid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    tarenombre = models.CharField(max_length = 255)
    taretipo = models.IntegerField()
    tarerestricgeo = models.CharField(max_length = 1000)
    tarerestriccant = models.IntegerField()
    tarerestrictime = models.CharField(max_length = 1000)
    instrid = models.UUIDField()
    proyid = models.UUIDField()
    dimensionid = models.UUIDField(null=True, blank=True)
    geojson_subconjunto = models.CharField(max_length=1000)
    tarefechacreacion = models.DateTimeField(null = True, blank = True, default=datetime.today())
    taredescripcion = models.TextField()
    tareestado = models.IntegerField(default=0)
    observaciones = models.TextField(blank = True, null = True)

    class Meta:
        db_table = '"v1"."tareas"'

##
# @brief Modelo de Dimensiones Geográficas
#
class DelimitacionGeografica(models.Model):

    dimensionid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    proyid = models.UUIDField()
    nombre = models.CharField(max_length=255)
    geojson = models.CharField(max_length=1000)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = '"v1"."dimensiones_territoriales"'

##
# @brief Modelo de Generos
#
class Genero(models.Model):

    generoid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)

    class Meta:
        db_table = '"v1"."generos"'

##
# @brief Modelo de Niveles educativos
#
class NivelEducativo(models.Model):

    nivelid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)

    class Meta:
        db_table = '"v1"."niveles_educativos"'

##
# @brief Modelo de barrios
#
class Barrio(models.Model):

    barrioid = models.IntegerField(editable=False, primary_key=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        db_table = '"v1"."barrios"'

##
# @brief Modelo de cartografias
#
class Cartografia(models.Model):

    cartografiaid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    instrid = models.UUIDField()
    osmid = models.CharField(max_length=255)
    elemosmid = models.UUIDField()
    userid = models.UUIDField()
    estado = models.IntegerField(default=0)
    tareid = models.UUIDField()

    class Meta:
        db_table = '"v1"."cartografias"'

##
# @brief Modelo de elementos de Open Street Maps
#
class ElementoOsm(models.Model):

    elemosmid = models.UUIDField(editable=False, primary_key=True)
    nombre = models.CharField(max_length=255)
    llaveosm = models.CharField(max_length=255)
    valorosm = models.CharField(max_length=255)
    closed_way = models.IntegerField()

    class Meta:
        db_table = '"v1"."elementos_osm"'

##
# @brief Modelo de Encuestas
#
class Encuesta(models.Model):
    
    encuestaid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    instrid = models.UUIDField()
    koboid = models.UUIDField()
    contenido = models.CharField(max_length=5000)
    estado = models.IntegerField(default=0)
    observacion = models.CharField(blank=True, max_length=3000, null=True)
    userid = models.UUIDField()
    tareid = models.UUIDField()
    
    class Meta:
        db_table = '"v1"."encuestas"'

##
# @brief Modelo de Conflictividades
#
class Conflictividad(models.Model):

    confid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = '"v1"."conflictividades"'

##
# @brief Modelo de los hechos asociados a las conflictividades
#
class Contextualizacion(models.Model):

    contxtid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    fecha_hecho = models.DateField()
    hora_hecho = models.TimeField()
    dia = models.IntegerField()
    confid = models.UUIDField()
    generoid = models.UUIDField()
    edad = models.IntegerField()
    nivelid = models.UUIDField()
    nombre_barrio = models.CharField(max_length=300)
    cantidad = models.IntegerField()
    barrioid = models.IntegerField()

    class Meta:
        db_table = '"v1"."contextualizaciones"'

##
# @brief Modelo de parámetros del sistema
#
class  Parametro(models.Model):

    paramid = models.CharField(max_length=1000, primary_key=True)
    paramvalor = models.CharField(max_length=1000)
    paramdesc = models.CharField(max_length=1000)

    class Meta:
        db_table = '"v1"."parametros"'

##
# @brief Modelo de historial de asignaciones de puntaje
#
class AsignacionPuntaje(models.Model):

    asigid = models.UUIDField(default = uuid.uuid4, primary_key=True)
    userid = models.UUIDField()
    tareid = models.UUIDField()
    puntaje = models.IntegerField()

    class Meta:
        db_table = '"v1"."asignaciones_puntajes"'

##
# @brief Modelo de plantillas de equipo
#
class PlantillaEquipo(models.Model):

    planid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    descripcion = models.TextField()
    userid = models.UUIDField()

    class Meta:
        db_table = '"v1"."plantillas_equipo"'

##
# @brief Modelo de miembros de plantilla
#
class MiembroPlantilla(models.Model):

    miplid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    userid = models.UUIDField()
    estado = models.IntegerField(default=1)
    planid = models.UUIDField()

    class Meta:
        db_table = '"v1"."miembros_plantilla"'

##
# @brief Modelo de Tipos de Proyecto
#
class TipoProyecto(models.Model):

    tiproid = models.UUIDField(default = uuid.uuid4, primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    class Meta:
        db_table = '"v1"."tipos_proyecto"'