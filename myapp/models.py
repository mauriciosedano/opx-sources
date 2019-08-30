from django.db import models
import uuid

class Usuario(models.Model):
    #userid = models.AutoField(primary_key = True)
    userid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False) 
    useremail = models.CharField(max_length = 255)
    userpassword = models.CharField(max_length = 255)
    usertoken = models.CharField(max_length = 255, null = True, blank = True)
    userfullname = models.CharField(max_length = 255)
    rolid = models.UUIDField()
    userleveltype = models.IntegerField()
    userestado = models.IntegerField()

    class Meta:
        db_table = '"v1"."usuarios"'


class DatosContexto(models.Model):

    dataid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    hdxtag = models.CharField(max_length = 20)
    datavalor = models.CharField(max_length = 20)
    datatipe = models.IntegerField()
    proyid = models.UUIDField()

    class Meta:
        db_table = '"v1"."datos_contexto"'


class Decision(models.Model):
    desiid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    desidescripcion = models.CharField(max_length = 1000)
    userid = models.UUIDField()

    class Meta:
        db_table = '"v1"."decisiones"'


class DecisionProyecto(models.Model):
    desproid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    proyid = models.UUIDField()
    desiid = models.UUIDField()

    class Meta:
        db_table = '"v1"."decisiones_proyecto"'


class Equipo(models.Model):
    equid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    userid = models.UUIDField()
    proyid = models.UUIDField()
    miembroestado = models.IntegerField()

    class Meta:
        db_table = '"v1"."equipos"'


class FuncionRol(models.Model):
    funcrolid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    rolid = models.UUIDField()
    actionid = models.CharField(max_length = 255)
    funcrolestado = models.IntegerField()
    funcrolpermiso = models.IntegerField()

    class Meta:
        db_table = '"v1"."funciones_rol"'


class Instrumento(models.Model):
    instrid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    instridexterno = models.CharField(max_length = 255)
    instrtipo = models.IntegerField()
    instrnombre = models.CharField(max_length = 255)
    instrdescripcion = models.CharField(max_length = 3000, null = True, blank = True)

    class Meta:
        db_table = '"v1"."instrumentos"'


class Proyecto(models.Model):
    proyid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    proynombre = models.CharField(max_length = 255)
    proydescripcion = models.CharField(max_length = 1000)
    proyidexterno = models.CharField(max_length = 255)
    proyfechacreacion = models.DateTimeField()
    proyfechacierre = models.DateTimeField(null = True, blank = True)
    proyestado = models.IntegerField()

    class Meta:
        db_table = '"v1"."proyectos"'


class Rol(models.Model):
    rolid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    rolname = models.CharField(max_length=50)
    roldescripcion = models.CharField(max_length = 255)
    rolestado = models.IntegerField()

    class Meta:
        db_table = '"v1"."roles"'


class Tarea(models.Model):

    tareid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    tarenombre = models.CharField(max_length = 255)
    taretipo = models.IntegerField()
    tarerestricgeo = models.CharField(max_length = 1000)
    tarerestriccant = models.IntegerField()
    tarerestrictime = models.CharField(max_length = 1000)
    instrid = models.UUIDField()
    proyid = models.UUIDField()

    class Meta:
        db_table = '"v1"."tareas"'