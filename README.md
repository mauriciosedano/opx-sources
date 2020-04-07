Documentación del Código Fuente

Neuromedia
==========

Indice de namespaces
====================

myapp.models

myapp.views

myapp.middleware.cors

myapp.view.auth

myapp.view.contextualizacion

myapp.view.equipo

myapp.view.estadisticas

myapp.view.notificaciones

myapp.view.osm

myapp.view.plantillaEquipo

myapp.view.proyecto

myapp.view.tareas

myapp.view.tiposProyecto

myapp.view.utilidades

Lista de clases
---------------

myapp.models.Accion (Modelo de Permisos del Sistema

myapp.models.AsignacionPuntaje (Modelo de historial de asignaciones de puntaje )

myapp.models.Barrio (Modelo de barrios )

myapp.models.Cartografia (Modelo de cartografias )

myapp.models.Conflictividad (Modelo de Conflictividades )

myapp.models.Contexto (Modelo de Contextos )

myapp.models.ContextoProyecto (Modelo de Contextos Proyecto )

myapp.models.Contextualizacion (Modelo de los hechos asociados a las
conflictividades )

cors.CorsMiddleware (Middleware que se encarga de agregar las cabeceras CORS con
el fin de permitir que el API REST sea consumida desde cualquier fuente )

myapp.models.DatosContexto (Modelo de Datos de Contexto )

myapp.models.Decision (Modelo de Decisiones )

myapp.models.DecisionProyecto (Modelo de Decisiones Proyecto )

myapp.models.DelimitacionGeografica (Modelo de Dimensiones Geográficas )

myapp.models.ElementoOsm (Modelo de elementos de Open Street Maps )

myapp.models.Encuesta (Modelo de Encuestas )

myapp.models.Equipo (Modelo de Equipos )

myapp.models.FuncionRol (Modelo de permisos para los roles )

myapp.models.Genero (Modelo de Generos )

myapp.models.Instrumento (Modelo de instrumentos )

myapp.models.MiembroPlantilla (Modelo de miembros de plantilla )

myapp.models.NivelEducativo (Modelo de Niveles educativos )

myapp.models.Parametro (Modelo de parámetros del sistema )

myapp.models.PlantillaEquipo (Modelo de plantillas de equipo )

myapp.models.Proyecto (Modelo de Proyectos )

myapp.models.Rol (Modelo de Roles del sistema )

myapp.models.Tarea (Modelo de Tareas )

myapp.models.TipoProyecto (Modelo de Tipos de Proyecto )

myapp.models.Usuario (Modelo de usuario )

Documentación de namespaces
===========================

Referencia del Namespace myapp.view.auth
----------------------------------------

### Funciones

-   def **passwordReset** (request)

*Plantilla de solicitud de Recuperación de Contraseña.*

-   def **passwordResetVerification** (request)

*Envio de Notificación de Correo para recuperación de contraseña.*

-   def **passwordResetConfirmation** (request, token)

*Plantilla de Cambio de Contraseña.*

-   def **passwordResetDone** (request)

*Plantilla para cambio de contraseña.*

### Documentación de las funciones

#### def auth.passwordReset ( *request*)

Plantilla de solicitud de Recuperación de Contraseña.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   plantilla HTML

#### def auth.passwordResetConfirmation ( *request*, *token*)

Plantilla de Cambio de Contraseña.

##### Parámetros

| *request* | instancia HttpRequest         |
|-----------|-------------------------------|
| *token*   | Token de Cambio de Contraseña |

##### Devuelve

>   plantilla HTML

#### def auth.passwordResetDone ( *request*)

Plantilla para cambio de contraseña.

##### Parámetros

| *request* | instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   Diccionario

#### def auth.passwordResetVerification ( *request*)

Envio de Notificación de Correo para recuperación de contraseña.

##### Parámetros

| *request* | instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   Diccionario

Referencia del Namespace myapp.view.contextualizacion
-----------------------------------------------------

### Funciones

-   def **categorizacion** (request)

*Indicadores de Conflictivades Por Categorias.*

-   def **todo** (request)

*Indicadores de conflictividades por Año.*

-   def **mensual** (request)

*Indicadores de conflictividades por Mes.*

-   def **semanal** (request)

*Indicadores de conflictividades por Semana.*

-   def **dia** (request)

*Indicadores de conflictividades por dia.*

-   def **calculoEdad** (born)

*Calculo de edad en base a una fecha de nacimiento.*

-   def **bisiesto** (ano, anio=True, mes=False)

*Cantidad de dias del mes o del año dependiendo de si es año bisiesto o no.*

-   def **verificacionExistenciaConflictividades** (cantidad)

*filtro final para proveer la cantidad de conflictividades*

### Documentación de las funciones

#### def contextualizacion.bisiesto ( *ano*, *anio* = True, *mes* = False)

Cantidad de dias del mes o del año dependiendo de si es año bisiesto o no.

##### Parámetros

| *ano*  | Año de referencia                                    |
|--------|------------------------------------------------------|
| *anio* | parametro opcional para activar verificacion del año |
| *mes*  | parametro opcional para activar verificación del mes |

##### Devuelve

>   numero entero correspondiente a la cantidad de dias

#### def contextualizacion.calculoEdad ( *born*)

Calculo de edad en base a una fecha de nacimiento.

##### Parámetros

| *born* | fecha de nacimiento del usuario |
|--------|---------------------------------|


##### Devuelve

>   numero entero con la edad del usuario

#### def contextualizacion.categorizacion ( *request*)

Indicadores de Conflictivades Por Categorias.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def contextualizacion.dia ( *request*)

Indicadores de conflictividades por dia.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def contextualizacion.mensual ( *request*)

Indicadores de conflictividades por Mes.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def contextualizacion.semanal ( *request*)

Indicadores de conflictividades por Semana.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def contextualizacion.todo ( *request*)

Indicadores de conflictividades por Año.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def contextualizacion.verificacionExistenciaConflictividades ( *cantidad*)

filtro final para proveer la cantidad de conflictividades

##### Parámetros

| *cantidad* | resultado de la consulta asociado a la cantidad de conflictividades |
|------------|---------------------------------------------------------------------|


##### Devuelve

>   numero entero correspondiente a la cantidad de conflictividades

Referencia del Namespace myapp.middleware.cors
----------------------------------------------

### Clases

-   class **CorsMiddleware**

*Middleware que se encarga de agregar las cabeceras CORS con el fin de permitir
que el API REST sea consumida desde cualquier fuente.*

Referencia del Namespace myapp.view.equipo
------------------------------------------

### Funciones

-   def **equipoProyecto** (request, proyid)

*Recurso que provee los integrantes de un proyecto.*

-   def **almacenamientoEquipo** (request)

*Recurso que asigna un voluntario/validador a un proyecto.*

-   def **eliminarEquipo** (request, equid)

*Recurso que elimina un integrante de equipo.*

-   def **actualizarEquipo** (request, equid)

*Recurso que actualiza el integrante de un equipo.*

-   def **usuariosDisponiblesProyecto** (request, proyid)

*Recurso que provee los usuarios disponibles para un proyecto.*

-   def **equipoProyectoView** (request, proyid)

*Plantilla para la gestión del equipo de un proyecto.*

### Documentación de las funciones

#### def equipo.actualizarEquipo ( *request*, *equid*)

Recurso que actualiza el integrante de un equipo.

##### Parámetros

| *request* | instancia HttpRequest                               |
|-----------|-----------------------------------------------------|
| *equid*   | Identificación de asignación de integrante a equipo |

##### Devuelve

>   cadena JSON

#### def equipo.almacenamientoEquipo ( *request*)

Recurso que asigna un voluntario/validador a un proyecto.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def equipo.eliminarEquipo ( *request*, *equid*)

Recurso que elimina un integrante de equipo.

##### Parámetros

| *request* | instancia HttpRequest                               |
|-----------|-----------------------------------------------------|
| *equid*   | Identificación de asignación de integrante a equipo |

##### Devuelve

>   cadena JSON

#### def equipo.equipoProyecto ( *request*, *proyid*)

Recurso que provee los integrantes de un proyecto.

##### Parámetros

| *request* | Instancia HttpRequest       |
|-----------|-----------------------------|
| *proyid*  | Identificacion del proyecto |

##### Devuelve

>   cadena JSON

#### def equipo.equipoProyectoView ( *request*, *proyid*)

Plantilla para la gestión del equipo de un proyecto.

##### Parámetros

| *request* | instancia HttpRequest         |
|-----------|-------------------------------|
| *proyid*  | Identificación de un proyecto |

##### Devuelve

>   cadena JSON

#### def equipo.usuariosDisponiblesProyecto ( *request*, *proyid*)

Recurso que provee los usuarios disponibles para un proyecto.

##### Parámetros

| *request* | instancia HttpRequest         |
|-----------|-------------------------------|
| *proyid*  | Identificación de un proyecto |

##### Devuelve

>   cadena JSON

Referencia del Namespace myapp.view.estadisticas
------------------------------------------------

### Funciones

-   def **datosGenerales** (request)

*Recurso que provee estadisticas generales del sistema.*

-   def **usuariosXRol** (request)

*Recurso que provee la cantidad de usuarios Por Rol del Sistema.*

-   def **usuariosXGenero** (request)

*Recurso que provee la cantidad de usuarios Por Sexo del Sistema.*

-   def **usuariosXNivelEducativo** (request)

*Recurso que provee la cantidad de usuarios Por Nivel Educativo del Sistema.*

-   def **usuariosXBarrio** (request)

*Recurso que provee la cantidad de usuarios Por Barrio del Sistema.*

-   def **tareasXTipo** (request)

*Recurso que provee la cantidad de tareas Por Tipo del Sistema.*

-   def **ranking** (request)

*Recurso que provee el ranking de usuarios del sistema.*

-   def **proyectosTareas** (request)

*Recurso que provee los proyectos y tareas del sistema que se encuentran en
ejecucion con el fin de mostrarlos en un diagrama de Gantt.*

-   def **estadoActualProyectos** (request)

*Recurso que provee informacion correspondiente al estado actual de los
proyectos que se encuentran en ejecución.*

-   def **proyectosTareasVencidos** (request)

*Recurso que provee los proyectos y tareas del sistema que se encuentran
terminados con el fin de mostrarlos en un diagrama de Gantt.*

-   def **estadoActualProyectosVencidos** (request)

*Recurso que provee informacion correspondiente al estado actual de los
proyectos que se encuentran terminados.*

-   def **tareasXTipoProyecto** (request, proyid)

*Recurso que provee la cantidad de tareas por tipo de un proyecto especifico.*

-   def **tareasXEstadoProyecto** (request, proyid)

*Recurso que provee la cantidad de tareas por estado de un proyecto especifico.*

-   def **usuariosXRolProyecto** (request, proyid)

*Recurso que provee la cantidad de usuarios por rol de un proyecto especifico.*

-   def **usuariosXBarrioProyecto** (request, proyid)

*Recurso que provee la cantidad de usuarios por barrio de un proyecto
especifico.*

-   def **usuariosXGeneroProyecto** (request, proyid)

*Recurso que provee la cantidad de usuarios por sexo de un proyecto especifico.*

-   def **usuariosXNivelEducativoProyecto** (request, proyid)

*Recurso que provee la cantidad de usuarios por nivel educativo de un proyecto
especifico.*

-   def **datosGeneralesProyecto** (request, proyid)

*Recurso que provee datos especificos de un proyecto.*

-   def **exportarDatos** (request, proyid)

*Recurso que provee un archivo que contiene las encuestas realizadas en un
proyecto.*

-   def **limpiezaDatos** (request, proyid)

*Script de ejemplo que tiene la capacidad de darle formato un archivo de
encuestas generado por el sistema.*

-   def **estadisticasView** (request)

*Plantilla de estadisticas generales del sistema.*

-   def **estadisticasDuranteView** (request)

*Plantilla de estadisticas correspondiente a los proyectos que se encuentran en
ejecución.*

-   def **estadisticasDespuesView** (request)

*Plantilla de estadisticas correspondiente a los proyectos que se encuentran
terminados.*

-   def **estadisticasDetalleView** (request, proyid)

*Plantilla de estadisticas correspondiente a un proyecto especifico.*

### Documentación de las funciones

#### def estadisticas.datosGenerales ( *request*)

Recurso que provee estadisticas generales del sistema.

##### Parámetros

| *request* | instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def estadisticas.datosGeneralesProyecto ( *request*, *proyid*)

Recurso que provee datos especificos de un proyecto.

>   Tales como: Cantidad de decisiones Cantidad de Contexto Cantidad de Campañas
>   Su convocatoria

##### Parámetros

| *request* | instancia HttpRequest       |
|-----------|-----------------------------|
| *proyid*  | Identificación del Proyecto |

##### Devuelve

>   cadena JSON

#### def estadisticas.estadisticasDespuesView ( *request*)

Plantilla de estadisticas correspondiente a los proyectos que se encuentran
terminados.

##### Parámetros

| *request* | instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   plantilla HTML

#### def estadisticas.estadisticasDetalleView ( *request*, *proyid*)

Plantilla de estadisticas correspondiente a un proyecto especifico.

##### Parámetros

| *request* | instancia HttpRequest         |
|-----------|-------------------------------|
| *proyid*  | Identificación de un proyecto |

##### Devuelve

>   plantilla HTML

#### def estadisticas.estadisticasDuranteView ( *request*)

Plantilla de estadisticas correspondiente a los proyectos que se encuentran en
ejecución.

##### Parámetros

| *request* | instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   plantilla HTML

#### def estadisticas.estadisticasView ( *request*)

Plantilla de estadisticas generales del sistema.

##### Parámetros

| *request* | instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   plantilla HTML

#### def estadisticas.estadoActualProyectos ( *request*)

Recurso que provee informacion correspondiente al estado actual de los proyectos
que se encuentran en ejecución.

>   Provee datos como: avance de ejecución avance de validacion cantidad de
>   integrantes

##### Parámetros

| *request* | instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def estadisticas.estadoActualProyectosVencidos ( *request*)

Recurso que provee informacion correspondiente al estado actual de los proyectos
que se encuentran terminados.

>   Provee datos como: avance de ejecución avance de validacion cantidad de
>   integrantes

##### Parámetros

| *request* | instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def estadisticas.exportarDatos ( *request*, *proyid*)

Recurso que provee un archivo que contiene las encuestas realizadas en un
proyecto.

##### Parámetros

| *request* | instancia HttpRequest       |
|-----------|-----------------------------|
| *proyid*  | Identificación del Proyecto |

##### Devuelve

>   cadena JSON

#### def estadisticas.limpiezaDatos ( *request*, *proyid*)

Script de ejemplo que tiene la capacidad de darle formato un archivo de
encuestas generado por el sistema.

##### Parámetros

| *request* | instancia HttpRequest       |
|-----------|-----------------------------|
| *proyid*  | Identificación del Proyecto |

##### Devuelve

>   cadena JSON

#### def estadisticas.proyectosTareas ( *request*)

Recurso que provee los proyectos y tareas del sistema que se encuentran en
ejecucion con el fin de mostrarlos en un diagrama de Gantt.

##### Parámetros

| *request* | instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def estadisticas.proyectosTareasVencidos ( *request*)

Recurso que provee los proyectos y tareas del sistema que se encuentran
terminados con el fin de mostrarlos en un diagrama de Gantt.

##### Parámetros

| *request* | instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def estadisticas.ranking ( *request*)

Recurso que provee el ranking de usuarios del sistema.

##### Parámetros

| *request* | instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def estadisticas.tareasXEstadoProyecto ( *request*, *proyid*)

Recurso que provee la cantidad de tareas por estado de un proyecto especifico.

##### Parámetros

| *request* | instancia HttpRequest       |
|-----------|-----------------------------|
| *proyid*  | Identificación del Proyecto |

##### Devuelve

>   cadena JSON

#### def estadisticas.tareasXTipo ( *request*)

Recurso que provee la cantidad de tareas Por Tipo del Sistema.

##### Parámetros

| *request* | instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def estadisticas.tareasXTipoProyecto ( *request*, *proyid*)

Recurso que provee la cantidad de tareas por tipo de un proyecto especifico.

##### Parámetros

| *request* | instancia HttpRequest       |
|-----------|-----------------------------|
| *proyid*  | Identificación del Proyecto |

##### Devuelve

>   cadena JSON

#### def estadisticas.usuariosXBarrio ( *request*)

Recurso que provee la cantidad de usuarios Por Barrio del Sistema.

##### Parámetros

| *request* | instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def estadisticas.usuariosXBarrioProyecto ( *request*, *proyid*)

Recurso que provee la cantidad de usuarios por barrio de un proyecto especifico.

##### Parámetros

| *request* | instancia HttpRequest       |
|-----------|-----------------------------|
| *proyid*  | Identificación del Proyecto |

##### Devuelve

>   cadena JSON

#### def estadisticas.usuariosXGenero ( *request*)

Recurso que provee la cantidad de usuarios Por Sexo del Sistema.

##### Parámetros

| *request* | instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def estadisticas.usuariosXGeneroProyecto ( *request*, *proyid*)

Recurso que provee la cantidad de usuarios por sexo de un proyecto especifico.

##### Parámetros

| *request* | instancia HttpRequest       |
|-----------|-----------------------------|
| *proyid*  | Identificación del Proyecto |

##### Devuelve

>   cadena JSON

#### def estadisticas.usuariosXNivelEducativo ( *request*)

Recurso que provee la cantidad de usuarios Por Nivel Educativo del Sistema.

##### Parámetros

| *request* | instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def estadisticas.usuariosXNivelEducativoProyecto ( *request*, *proyid*)

Recurso que provee la cantidad de usuarios por nivel educativo de un proyecto
especifico.

##### Parámetros

| *request* | instancia HttpRequest       |
|-----------|-----------------------------|
| *proyid*  | Identificación del Proyecto |

##### Devuelve

>   cadena JSON

#### def estadisticas.usuariosXRol ( *request*)

Recurso que provee la cantidad de usuarios Por Rol del Sistema.

##### Parámetros

| *request* | instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def estadisticas.usuariosXRolProyecto ( *request*, *proyid*)

Recurso que provee la cantidad de usuarios por rol de un proyecto especifico.

##### Parámetros

| *request* | instancia HttpRequest       |
|-----------|-----------------------------|
| *proyid*  | Identificación del Proyecto |

##### Devuelve

>   cadena JSON

Referencia del Namespace myapp.models
-------------------------------------

### Clases

-   class **Accion**

*Modelo de Permisos del Sistema.*

-   class **AsignacionPuntaje**

*Modelo de historial de asignaciones de puntaje.*

-   class **Barrio**

*Modelo de barrios.*

-   class **Cartografia**

*Modelo de cartografias.*

-   class **Conflictividad**

*Modelo de Conflictividades.*

-   class **Contexto**

*Modelo de Contextos.*

-   class **ContextoProyecto**

*Modelo de Contextos Proyecto.*

-   class **Contextualizacion**

*Modelo de los hechos asociados a las conflictividades.*

-   class **DatosContexto**

*Modelo de Datos de Contexto.*

-   class **Decision**

*Modelo de Decisiones.*

-   class **DecisionProyecto**

*Modelo de Decisiones Proyecto.*

-   class **DelimitacionGeografica**

*Modelo de Dimensiones Geográficas.*

-   class **ElementoOsm**

*Modelo de elementos de Open Street Maps.*

-   class **Encuesta**

*Modelo de Encuestas.*

-   class **Equipo**

*Modelo de Equipos.*

-   class **FuncionRol**

*Modelo de permisos para los roles.*

-   class **Genero**

*Modelo de Generos.*

-   class **Instrumento**

*Modelo de instrumentos.*

-   class **MiembroPlantilla**

*Modelo de miembros de plantilla.*

-   class **MyUserManager**

-   class **NivelEducativo**

*Modelo de Niveles educativos.*

-   class **Parametro**

*Modelo de parámetros del sistema.*

-   class **PlantillaEquipo**

*Modelo de plantillas de equipo.*

-   class **Proyecto**

*Modelo de Proyectos.*

-   class **Rol**

*Modelo de Roles del sistema.*

-   class **Tarea**

*Modelo de Tareas.*

-   class **TipoProyecto**

*Modelo de Tipos de Proyecto.*

-   class **Usuario**

*Modelo de usuario.*

Referencia del Namespace myapp.views
------------------------------------

### Funciones

-   def **loginView** (request)

*Vista de Autenticación Dashboard.*

-   def **login** (request)

*Recurso de Autenticación de Usuarios.*

-   def **listadoUsuarios** (request)

*Recurso de listado de usuarios.*

-   def **detalleUsuario** (request, userid)

*Recurso que provee el detalle de un usuario registrado.*

-   def **almacenarUsuario** (request)

*Recurso de almacenamiento de usuarios.*

-   def **eliminarUsuario** (request, userid)

*Recurso de eliminación de usuarios.*

-   def **actualizarUsuario** (request, userid)

*Recurso de Actualización de usuarios.*

-   def **listadoUsuariosView** (request)

*plantilla de listado de usuarios*

-   def **listadoContextos** (request)

*Recurso de listado de contextos.*

-   def **almacenamientoContexto** (request)

*Recurso de almacenamiento de contextos.*

-   def **eliminarContexto** (request, contextoid)

*Recurso de eliminación de contextos.*

-   def **actualizarContexto** (request, contextoid)

*Recurso de actualización de contextos.*

-   def **listadoContextosView** (request)

*Plantilla HTML de contextos.*

-   def **geopandaGeojson** (geometry)

*Convierte feature de Mapa a GeoJSON.*

-   def **listadoDatosContextoCompleto** (request)

*Recurso de listado de datos de contexto.*

-   def **listadoDatosContexto** (request, contextoid)

*Recurso de listado de datos de contexto por contexto.*

-   def **almacenarDatoContexto** (request)

*Recurso de almacenamiento de datos de contexto.*

-   def **eliminarDatoContexto** (request, dataid)

*Recurso de eliminación de datos de contexto.*

-   def **actualizarDatoContexto** (request, dataid)

*Recurso de actualización de datos de contexto.*

-   def **listadoDatosContextoView** (request, contextoid)

*Plantilla de datos de contexto.*

-   def **listadoDecisiones** (request)

*Recurso de listado de decisiones.*

-   def **almacenarDecision** (request)

*Recurso de almacenamiento de decisiones.*

-   def **eliminarDecision** (request, desiid)

*Recurso de eliminación de decisiones.*

-   def **actualizarDecision** (request, desiid)

*Recurso de actualización de decisiones.*

-   def **listadoDecisionesView** (request)

*Plantilla de decisiones.*

-   def **listadoDecisionesProyecto** (request)

*Recurso de listado de decisiones Proyecto.*

-   def **eliminarDecisionProyecto** (request, desproid)

*Recurso de eliminación de decisiones Proyecto.*

-   def **actualizarDecisionProyecto** (request, desproid)

*Recurso de actualización de decisiones Proyecto.*

-   def **listadoAcciones** (request)

*Recurso de listado de Funciones del Sistema.*

-   def **listadoFuncionesRol** (request, rolid)

*Recurso de listado de Funciones del Sistema para un rol.*

-   def **almacenamientoFuncionRol** (request)

*Recurso para añadir Funciones del Sistema a un rol.*

-   def **eliminarFuncionRol** (request, funcrolid)

*Recurso para eliminar Funciones del Sistema a un Rol.*

-   def **actualizarFuncionRol** (request, funcrolid)

*Recurso de actualización de Funcion del Sistema a un rol.*

-   def **listadoInstrumentos** (request)

*Recurso de listado de instrumentos.*

-   def **almacenamientoInstrumento** (request)

*Recurso de almacenamiento de Instrumento.*

-   def **eliminarInstrumento** (request, instrid)

*Recurso para eliminación de instrumentos.*

-   def **actualizarInstrumento** (request, instrid)

*Recurso de actualización de Instrumentos.*

-   def **almacenarEncuestas** (instrumento, informacion, userid, tareid)

*Recurso de almacenamiento de encuestas.*

-   def **revisarEncuesta** (request, encuestaid)

*Revisión del estado de una encuesta.*

-   def **informacionInstrumento** (request, id)

*Recurso para obtener información de instrumentos.*

-   def **listadoInstrumentosView** (request)

*Plantilla de Instrumentos.*

-   def **informacionInstrumentoView** (request, id)

*Plantilla para información de Instrumento.*

-   def **creacionEncuestaView** (request)

*Plantilla de creación de Encuesta.*

-   def **listadoRoles** (request)

*Recurso de Listao de Roles.*

-   def **almacenamientoRol** (request)

*Recurso de almacenamiento de Roles.*

-   def **eliminarRol** (request, rolid)

*Recurso de eliminación de Roles.*

-   def **actualizarRol** (request, rolid)

*Recurso de actualización de Roles.*

-   def **listadoRolesView** (request)

*Plantilla de Roles.*

-   def **permisosRolView** (request, rolid)

*Plantilla de Funcionalidades del sistema para un rol.*

-   def **informacionFormularioKoboToolbox** (id)

*Obtenención de encuestas de un formulario KoboToolbox.*

-   def **detalleFormularioKoboToolbox** (id)

*Obtención de información de detalle de un formulario de KoboToolbox.*

-   def **enlaceFormularioKoboToolbox** (request, tareid)

*Obtención de enlace de diligenciamiento de un formulario de KoboToolbox.*

-   def **implementarFormularioKoboToolbox** (request, id)

*Implementación/Despliegue de un formulario de KoboToolbox.*

-   def **listadoFormulariosKoboToolbox** (request)

*Listado de formularios de KoboToolbox.*

-   def **verificarImplementaciónFormulario** (request, id)

*Verificación de Implementación/Despliegue de un formulario de KoboToolbox.*

-   def **almacenarProyectoTM** (nombre, areaInteres)

*Almacenamiento de Proyecto de Mapeo en Tasking Manager.*

-   def **informacionProyectoTM** (id)

*Obtención de información de detalle de un Proyecto de Mapeo de Tasking
Manager.*

-   def **perfilView** (request)

*Plantilla de Perfil de Usuario.*

### Documentación de las funciones

#### def myapp.views.actualizarContexto ( *request*, *contextoid*)

Recurso de actualización de contextos.

##### Parámetros

| *request*    | Instancia HttpRequest       |
|--------------|-----------------------------|
| *contextoid* | Identificación del Contexto |

##### Devuelve

>   cadena JSON

#### def myapp.views.actualizarDatoContexto ( *request*, *dataid*)

Recurso de actualización de datos de contexto.

##### Parámetros

| *request* | Instancia HttpRequest              |
|-----------|------------------------------------|
| *dataid*  | Identificación de dato de contexto |

##### Devuelve

>   cadena JSON

#### def myapp.views.actualizarDecision ( *request*, *desiid*)

Recurso de actualización de decisiones.

##### Parámetros

| *request* | Instancia HttpRequest param desiid Identificación de la decisión |
|-----------|------------------------------------------------------------------|


##### Devuelve

>   cadena JSON

#### def myapp.views.actualizarDecisionProyecto ( *request*, *desproid*)

Recurso de actualización de decisiones Proyecto.

##### Parámetros

| *request*  | Instancia HttpRequest               |
|------------|-------------------------------------|
| *desproid* | Identificación de Decisión Proyecto |

##### Devuelve

>   cadena JSON

#### def myapp.views.actualizarFuncionRol ( *request*, *funcrolid*)

Recurso de actualización de Funcion del Sistema a un rol.

##### Parámetros

| *request*   | Instancia HttpRequest                                        |
|-------------|--------------------------------------------------------------|
| *funcrolid* | Identificación de asignación de funcion del sistema a un rol |

##### Devuelve

>   cadena JSON

#### def myapp.views.actualizarInstrumento ( *request*, *instrid*)

Recurso de actualización de Instrumentos.

##### Parámetros

| *request* | Instancia HttpRequest          |
|-----------|--------------------------------|
| *instrid* | Identificación del Instrumento |

##### Devuelve

>   cadena JSON

#### def myapp.views.actualizarRol ( *request*, *rolid*)

Recurso de actualización de Roles.

##### Parámetros

| *request* | Instancia HttpRequest  |
|-----------|------------------------|
| *rolid*   | Identificación del Rol |

##### Devuelve

>   cadena JSON

#### def myapp.views.actualizarUsuario ( *request*, *userid*)

Recurso de Actualización de usuarios.

##### Parámetros

| *request* | Instancia HttpRequest                 |
|-----------|---------------------------------------|
| *userid*  | Identificación de usuario autenticado |

##### Devuelve

>   cadena JSON

#### def myapp.views.almacenamientoContexto ( *request*)

Recurso de almacenamiento de contextos.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def myapp.views.almacenamientoFuncionRol ( *request*)

Recurso para añadir Funciones del Sistema a un rol.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def myapp.views.almacenamientoInstrumento ( *request*)

Recurso de almacenamiento de Instrumento.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def myapp.views.almacenamientoRol ( *request*)

Recurso de almacenamiento de Roles.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def myapp.views.almacenarDatoContexto ( *request*)

Recurso de almacenamiento de datos de contexto.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def myapp.views.almacenarDecision ( *request*)

Recurso de almacenamiento de decisiones.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def myapp.views.almacenarEncuestas ( *instrumento*, *informacion*, *userid*, *tareid*)

Recurso de almacenamiento de encuestas.

##### Parámetros

| *instrumento* | Instancia modelo Instrumento     |
|---------------|----------------------------------|
| *informacion* | dataset de encuestas a almacenar |
| *userid*      | Identificación del usuario       |
| *tareid*      | Identificación de la tarea       |

##### Devuelve

>   Diccionario

#### def myapp.views.almacenarProyectoTM ( *nombre*, *areaInteres*)

Almacenamiento de Proyecto de Mapeo en Tasking Manager.

##### Parámetros

| *nombre* | nombre del Proyecto areaInteres geoJSON que describe el área de trabajo de un proyecto de Mapeo |
|----------|-------------------------------------------------------------------------------------------------|


##### Devuelve

>   Diccionario

#### def myapp.views.almacenarUsuario ( *request*)

Recurso de almacenamiento de usuarios.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def myapp.views.creacionEncuestaView ( *request*)

Plantilla de creación de Encuesta.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   Plantilla HTML

#### def myapp.views.detalleFormularioKoboToolbox ( *id*)

Obtención de información de detalle de un formulario de KoboToolbox.

##### Parámetros

| *id* | Identificación del Formulario KoboToolbox |
|------|-------------------------------------------|


##### Devuelve

>   Diccionario

#### def myapp.views.detalleUsuario ( *request*, *userid*)

Recurso que provee el detalle de un usuario registrado.

##### Parámetros

| *userid* | identificación del usuario |
|----------|----------------------------|


##### Devuelve

>   Cadena JSON

#### def myapp.views.eliminarContexto ( *request*, *contextoid*)

Recurso de eliminación de contextos.

##### Parámetros

| *request*    | Instancia HttpRequest       |
|--------------|-----------------------------|
| *contextoid* | Identificación del contexto |

##### Devuelve

>   cadena JSON

#### def myapp.views.eliminarDatoContexto ( *request*, *dataid*)

Recurso de eliminación de datos de contexto.

##### Parámetros

| *request* | Instancia HttpRequest              |
|-----------|------------------------------------|
| *dataid*  | Identificación de dato de contexto |

##### Devuelve

>   cadena JSON

#### def myapp.views.eliminarDecision ( *request*, *desiid*)

Recurso de eliminación de decisiones.

##### Parámetros

| *request* | Instancia HttpRequest         |
|-----------|-------------------------------|
| *desiid*  | Identificación de la decisión |

##### Devuelve

>   cadena JSON

#### def myapp.views.eliminarDecisionProyecto ( *request*, *desproid*)

Recurso de eliminación de decisiones Proyecto.

##### Parámetros

| *request*  | Instancia HttpRequest               |
|------------|-------------------------------------|
| *desproid* | Identificación de Decision Proyecto |

##### Devuelve

>   cadena JSON

#### def myapp.views.eliminarFuncionRol ( *request*, *funcrolid*)

Recurso para eliminar Funciones del Sistema a un Rol.

##### Parámetros

| *request*   | Instancia HttpRequest                                        |
|-------------|--------------------------------------------------------------|
| *funcrolid* | Identificación de asignación de funcion del sistema a un rol |

##### Devuelve

>   cadena JSON

#### def myapp.views.eliminarInstrumento ( *request*, *instrid*)

Recurso para eliminación de instrumentos.

##### Parámetros

| *request* | Instancia HttpRequest          |
|-----------|--------------------------------|
| *instrid* | Identificación del Instrumento |

##### Devuelve

>   cadena JSON

#### def myapp.views.eliminarRol ( *request*, *rolid*)

Recurso de eliminación de Roles.

##### Parámetros

| *request* | Instancia HttpRequest  |
|-----------|------------------------|
| *rolid*   | Identificación del Rol |

##### Devuelve

>   cadena JSON

#### def myapp.views.eliminarUsuario ( *request*, *userid*)

Recurso de eliminación de usuarios.

##### Parámetros

| *request* | Instancia HttpRequest                 |
|-----------|---------------------------------------|
| *userid*  | Identificación de usuario autenticado |

##### Devuelve

>   cadena JSON

#### def myapp.views.enlaceFormularioKoboToolbox ( *request*, *tareid*)

Obtención de enlace de diligenciamiento de un formulario de KoboToolbox.

##### Parámetros

| *id* | tareid Identificación de la tarea Tipo Encuesta |
|------|-------------------------------------------------|


##### Devuelve

>   cadena JSON

#### def myapp.views.geopandaGeojson ( *geometry*)

Convierte feature de Mapa a GeoJSON.

##### Parámetros

| *geometry* | Feature de Mapa - Puede ser Punto o Poligono |
|------------|----------------------------------------------|


##### Devuelve

>   GeoJSON

#### def myapp.views.implementarFormularioKoboToolbox ( *request*, *id*)

Implementación/Despliegue de un formulario de KoboToolbox.

##### Parámetros

| *id* | Identificación del Formulario KoboToolbox |
|------|-------------------------------------------|


##### Devuelve

>   cadena JSON

#### def myapp.views.informacionFormularioKoboToolbox ( *id*)

Obtenención de encuestas de un formulario KoboToolbox.

##### Parámetros

| *id* | Identificación del Formulario KoboToolbox |
|------|-------------------------------------------|


##### Devuelve

>   Diccionario

#### def myapp.views.informacionInstrumento ( *request*, *id*)

Recurso para obtener información de instrumentos.

##### Parámetros

| *request* | Instancia HttpRequest           |
|-----------|---------------------------------|
| *id*      | Indentificación del instrumento |

##### Devuelve

>   cadena JSON

#### def myapp.views.informacionInstrumentoView ( *request*, *id*)

Plantilla para información de Instrumento.

##### Parámetros

| *request* | Instancia HttpRequest          |
|-----------|--------------------------------|
| *id*      | Identificación del instrumento |

##### Devuelve

>   Plantilla HTML

#### def myapp.views.informacionProyectoTM ( *id*)

Obtención de información de detalle de un Proyecto de Mapeo de Tasking Manager.

##### Parámetros

| *id* | Identificación del proyecto de Mapeo Tasking Manager |
|------|------------------------------------------------------|


##### Devuelve

>   Diccionario

#### def myapp.views.listadoAcciones ( *request*)

Recurso de listado de Funciones del Sistema.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def myapp.views.listadoContextos ( *request*)

Recurso de listado de contextos.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def myapp.views.listadoContextosView ( *request*)

Plantilla HTML de contextos.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   plantilla HTML

#### def myapp.views.listadoDatosContexto ( *request*, *contextoid*)

Recurso de listado de datos de contexto por contexto.

##### Parámetros

| *request*    | Instancia HttpRequest       |
|--------------|-----------------------------|
| *contextoid* | Identificación del Contexto |

##### Devuelve

>   cadena JSON

#### def myapp.views.listadoDatosContextoCompleto ( *request*)

Recurso de listado de datos de contexto.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def myapp.views.listadoDatosContextoView ( *request*, *contextoid*)

Plantilla de datos de contexto.

##### Parámetros

| *request*    | Instancia HttpRequest       |
|--------------|-----------------------------|
| *contextoid* | Identificación del contexto |

##### Devuelve

>   Plantilla HTML

#### def myapp.views.listadoDecisiones ( *request*)

Recurso de listado de decisiones.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def myapp.views.listadoDecisionesProyecto ( *request*)

Recurso de listado de decisiones Proyecto.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def myapp.views.listadoDecisionesView ( *request*)

Plantilla de decisiones.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   plantilla HTML

#### def myapp.views.listadoFormulariosKoboToolbox ( *request*)

Listado de formularios de KoboToolbox.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def myapp.views.listadoFuncionesRol ( *request*, *rolid*)

Recurso de listado de Funciones del Sistema para un rol.

##### Parámetros

| *request* | Instancia HttpRequest             |
|-----------|-----------------------------------|
| *rolid*   | Identificación del rol de usuario |

##### Devuelve

>   cadena JSON

#### def myapp.views.listadoInstrumentos ( *request*)

Recurso de listado de instrumentos.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def myapp.views.listadoInstrumentosView ( *request*)

Plantilla de Instrumentos.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   Plantilla HTML

#### def myapp.views.listadoRoles ( *request*)

Recurso de Listao de Roles.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def myapp.views.listadoRolesView ( *request*)

Plantilla de Roles.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   plantilla HTML

#### def myapp.views.listadoUsuarios ( *request*)

Recurso de listado de usuarios.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def myapp.views.listadoUsuariosView ( *request*)

plantilla de listado de usuarios

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   plantilla HTML

#### def myapp.views.login ( *request*)

Recurso de Autenticación de Usuarios.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def myapp.views.loginView ( *request*)

Vista de Autenticación Dashboard.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   Plantilla Html

#### def myapp.views.perfilView ( *request*)

Plantilla de Perfil de Usuario.

##### Parámetros

| *request* | instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   plantilla HTML

#### def myapp.views.permisosRolView ( *request*, *rolid*)

Plantilla de Funcionalidades del sistema para un rol.

##### Parámetros

| *request* | Instancia HttpRequest  |
|-----------|------------------------|
| *rolid*   | Identificación del rol |

##### Devuelve

>   cadena JSON

#### def myapp.views.revisarEncuesta ( *request*, *encuestaid*)

Revisión del estado de una encuesta.

##### Parámetros

| *request*    | Instancia HttpRequest         |
|--------------|-------------------------------|
| *encuestaid* | Identificación de la encuesta |

##### Devuelve

>   cadena JSON

#### def myapp.views.verificarImplementaciónFormulario ( *request*, *id*)

Verificación de Implementación/Despliegue de un formulario de KoboToolbox.

##### Parámetros

| *request* | Instancia HttpRequest                     |
|-----------|-------------------------------------------|
| *id*      | Identificación del Formulario KoboToolbox |

##### Devuelve

>   cadena JSON

Referencia del Namespace myapp.notificaciones
---------------------------------------------

### Funciones

-   def **gestionCambios** (usuarios, tipoReceptor, nombreReceptor, tipoCambio,
    detalle="")

*Envio de notifificaciones correspondiente a la gestión de cambios de un
proyecto especifico.*

### Documentación de las funciones

#### def notificaciones.gestionCambios ( *usuarios*, *tipoReceptor*, *nombreReceptor*, *tipoCambio*, *detalle* = "")

Envio de notifificaciones correspondiente a la gestión de cambios de un proyecto
especifico.

##### Parámetros

| *usuarios*       | lista de correos electrónicos destinatarios de la notificación  |
|------------------|-----------------------------------------------------------------|
| *tipoReceptor*   | define el tipo de entidad que sufrio cambios (proyecto o tarea) |
| *nombreReceptor* | define el nombre del proyecto/tarea que sufrio cambios          |
| *tipoCambio*     | Define el tipo de cambio que sufrio el proyecto/tarea.          |
| *detalle*        | información adicional del cambio efectuado                      |

##### Devuelve

>   cadena JSON

Referencia del Namespace myapp.osm
----------------------------------

### Funciones

-   def **osmHeaders** ()

*Función que provee las cabeceras que requiere el API REST de Open Street Maps.*

-   def **agregarChangeset** ()

*Función que agrega un nuevo changeset en Open Street Maps.*

-   def **cerrarChangeset** (changeset)

*Funcion que cierre Changeset en Open Street Maps.*

-   def **AgregarElemento** (request, tareid)

*Recurso que agrega elemento en Open Street Maps.*

-   def **almacenarCartografia** (instrid, wayid, elemosmid, userid, tareid)

*Funcion que asocia la cartografia realizada en Open Street Maps al sistema.*

-   def **elementosOsm** (request)

*Recurso que provee los tipos de elementos de Open Street Maps Disponibles.*

-   def **detalleCartografia** (tareid)

*Funcion que provee en formato GeoJSON las cartografias realizadas en una
tarea.*

-   def **cartografiasInstrumento** (request, tareid)

*Recurso que provee las cartografias realizadas en una tarea.*

-   def **eliminarCartografia** (request, cartografiaid)

*Recurso que elimina un aporte cartográfico del sistema.*

### Variables

-   **osmRestApiUrl** = settings['osm-api-url']

### Documentación de las funciones

#### def osm.agregarChangeset ()

Función que agrega un nuevo changeset en Open Street Maps.

##### Devuelve

>   Respuesta de API de Open Street Maps

#### def osm.AgregarElemento ( *request*, *tareid*)

Recurso que agrega elemento en Open Street Maps.

##### Parámetros

| *request* | Instancia HttpRequest      |
|-----------|----------------------------|
| *tareid*  | Identificación de la tarea |

##### Devuelve

>   Cadena JSON

#### def osm.almacenarCartografia ( *instrid*, *wayid*, *elemosmid*, *userid*, *tareid*)

Funcion que asocia la cartografia realizada en Open Street Maps al sistema.

##### Parámetros

| *instrid*   | Identificación del Instrumento                           |
|-------------|----------------------------------------------------------|
| *wayid*     | Identificación del elemento agregado en Open Street Maps |
| *elemosmid* | Identificación de tipo de elemento de Open Street Maps   |
| *userid*    | Identificación del usuario que realizo la cartografia    |
| *tareid*    | Identificación de la tarea                               |

##### Devuelve

>   Diccionario con la información de la cartografia realizada

#### def osm.cartografiasInstrumento ( *request*, *tareid*)

Recurso que provee las cartografias realizadas en una tarea.

##### Parámetros

| *request* | Instancia HttpRequest      |
|-----------|----------------------------|
| *tareid*  | Identificación de la tarea |

##### Devuelve

>   cadena JSON

#### def osm.cerrarChangeset ( *changeset*)

Funcion que cierre Changeset en Open Street Maps.

##### Parámetros

| *changeset* | abierto de Open Street Maps |
|-------------|-----------------------------|


##### Devuelve

>   Respuesta de API de Open Street Maps

#### def osm.detalleCartografia ( *tareid*)

Funcion que provee en formato GeoJSON las cartografias realizadas en una tarea.

##### Parámetros

| *tareid* | Identificación de la tarea |
|----------|----------------------------|


##### Devuelve

>   Diccionario

#### def osm.elementosOsm ( *request*)

Recurso que provee los tipos de elementos de Open Street Maps Disponibles.

##### Parámetros

| *request* | instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def osm.eliminarCartografia ( *request*, *cartografiaid*)

Recurso que elimina un aporte cartográfico del sistema.

##### Parámetros

| *request*       | Instancia HttpRequest            |
|-----------------|----------------------------------|
| *cartografiaid* | Identificación de la cartografia |

##### Devuelve

>   cadena JSON

#### def osm.osmHeaders ()

Función que provee las cabeceras que requiere el API REST de Open Street Maps.

##### Devuelve

>   Diccionario

### Documentación de las variables

#### osm.osmRestApiUrl = settings['osm-api-url']

Referencia del Namespace myapp.plantillaEquipo
----------------------------------------------

### Funciones

-   def **listadoPlantillas** (request)

*Recurso de listado de plantillas de equipo.*

-   def **eliminarPlantilla** (request, planid)

*Recurso de eliminación de plantilla de equipo.*

-   def **crearPlantilla** (request)

*Recurso de creación de plantilla de equipo.*

-   def **edicionPlantilla** (request, planid)

*Recurso de edición de plantilla de equipo.*

-   def **miembrosPlantilla** (request, planid)

*Recurso de listado de integrantes de una plantilla de equipo.*

-   def **agregarMiembro** (request, planid)

*Recurso de Inserción de usuario a una plantilla de equipo.*

-   def **eliminarMiembro** (request, miplid)

*Recurso de eliminación de usuario de una plantilla de equipo.*

-   def **miembrosDisponibles** (request, planid)

*Recurso que provee el listado de usuarios que se pueden agregar a una plantilla
de equipo.*

-   def **plantillasView** (request)

*Función que provee plantilla HTML para gestión de plantillas de equipo.*

-   def **miembrosPlantillaView** (request, planid)

*Función que provee plantilla HTML para gestión de integrantes de plantillas de
equipo.*

### Documentación de las funciones

#### def plantillaEquipo.agregarMiembro ( *request*, *planid*)

Recurso de Inserción de usuario a una plantilla de equipo.

##### Parámetros

| *request* | Instancia HttpRequest                 |
|-----------|---------------------------------------|
| *planid*  | Identificación de plantilla de equipo |

##### Devuelve

>   cadena JSON

#### def plantillaEquipo.crearPlantilla ( *request*)

Recurso de creación de plantilla de equipo.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def plantillaEquipo.edicionPlantilla ( *request*, *planid*)

Recurso de edición de plantilla de equipo.

##### Parámetros

| *request* | Instancia HttpRequest                 |
|-----------|---------------------------------------|
| *planid*  | Identificación de plantilla de Equipo |

##### Devuelve

>   cadena JSON

#### def plantillaEquipo.eliminarMiembro ( *request*, *miplid*)

Recurso de eliminación de usuario de una plantilla de equipo.

##### Parámetros

| *request* | Instancia HttpRequest                                         |
|-----------|---------------------------------------------------------------|
| *miplid*  | Identificación de asignación de usuario a plantilla de equipo |

##### Devuelve

>   cadena JSON

#### def plantillaEquipo.eliminarPlantilla ( *request*, *planid*)

Recurso de eliminación de plantilla de equipo.

##### Parámetros

| *request* | Instancia HttpRequest                 |
|-----------|---------------------------------------|
| *planid*  | Identificación de Plantilla de Equipo |

##### Devuelve

>   cadena JSON

#### def plantillaEquipo.listadoPlantillas ( *request*)

Recurso de listado de plantillas de equipo.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def plantillaEquipo.miembrosDisponibles ( *request*, *planid*)

Recurso que provee el listado de usuarios que se pueden agregar a una plantilla
de equipo.

##### Parámetros

| *request* | Instancia HttpRequest                 |
|-----------|---------------------------------------|
| *planid*  | Identificación de plantilla de equipo |

##### Devuelve

>   cadena JSON

#### def plantillaEquipo.miembrosPlantilla ( *request*, *planid*)

Recurso de listado de integrantes de una plantilla de equipo.

##### Parámetros

| *request* | Instancia HttpRequest                 |
|-----------|---------------------------------------|
| *planid*  | Identificación de plantilla de equipo |

##### Devuelve

>   cadena JSON

#### def plantillaEquipo.miembrosPlantillaView ( *request*, *planid*)

Función que provee plantilla HTML para gestión de integrantes de plantillas de
equipo.

##### Parámetros

| *request* | Instancia HttpRequest                 |
|-----------|---------------------------------------|
| *planid*  | Identificación de plantilla de equipo |

##### Devuelve

>   plantilla HTML

#### def plantillaEquipo.plantillasView ( *request*)

Función que provee plantilla HTML para gestión de plantillas de equipo.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   plantilla HTML

Referencia del Namespace myapp.proyecto
---------------------------------------

### Funciones

-   def **listadoProyectos** (request)

*Recurso de listado de proyectos.*

-   def **almacenamientoProyecto** (request)

*Recurso de almacenamiento de proyectos.*

-   def **almacenarDecisionProyecto** (proyecto, decisiones)

*Funcion que asigna decision(es) a un proyecto especifico.*

-   def **almacenarContextosProyecto** (proyecto, contextos)

*Funcion que asigna contexto(s) a un proyecto especifico.*

-   def **almacenarDelimitacionesGeograficas** (proyecto,
    delimitacionesGeograficas)

*Funcion que almacena las dimensiones geograficas de un proyecto especifico.*

-   def **asignarEquipos** (proyecto, equipos)

*Funcion que asigna integrantes a un proyecto en base a los integrantes de una
plantilla de equipo.*

-   def **eliminarProyecto** (request, proyid)

*recurso de eliminación de proyectos*

-   def **actualizarProyecto** (request, proyid)

*recurso de actualización de proyectos*

-   def **detalleProyecto** (request, proyid)

*recurso que provee el detalle de un proyecto*

-   def **dimensionesTerritoriales** (request, proyid)

*recurso que provee las dimensiones geograficas de un proyecto*

-   def **cambioTerritorio** (request, dimensionid)

*recurso de cambio de territorio de dimensiones geograficas y tareas de un
proyecto*

-   def **listadoProyectosView** (request)

*Función que provee una plantilla HTML para la gestión de proyectos.*

-   def **gestionProyectosView** (request)

*Función que provee una plantilla HTML para la gestión de cambios de un
proyecto.*

-   def **tareasProyectoView** (request, proyid)

*Función que provee una plantilla HTML para la gestión de tareas de un proyecto
especifico.*

### Documentación de las funciones

#### def proyecto.actualizarProyecto ( *request*, *proyid*)

recurso de actualización de proyectos

##### Parámetros

| *request* | Instancia HttpRequest       |
|-----------|-----------------------------|
| *proyid*  | Identificación del proyecto |

##### Devuelve

>   cadena JSON

#### def proyecto.almacenamientoProyecto ( *request*)

Recurso de almacenamiento de proyectos.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def proyecto.almacenarContextosProyecto ( *proyecto*, *contextos*)

Funcion que asigna contexto(s) a un proyecto especifico.

##### Parámetros

| *proyecto*  | instancia del modelo proyecto           |
|-------------|-----------------------------------------|
| *contextos* | listado de identificadores de contextos |

##### Devuelve

>   booleano

#### def proyecto.almacenarDecisionProyecto ( *proyecto*, *decisiones*)

Funcion que asigna decision(es) a un proyecto especifico.

##### Parámetros

| *proyecto*   | instancia del modelo proyecto            |
|--------------|------------------------------------------|
| *decisiones* | listado de identificadores de decisiones |

##### Devuelve

>   booleano

#### def proyecto.almacenarDelimitacionesGeograficas ( *proyecto*, *delimitacionesGeograficas*)

Funcion que almacena las dimensiones geograficas de un proyecto especifico.

##### Parámetros

| *proyecto*                  | instancia del modelo proyecto                    |
|-----------------------------|--------------------------------------------------|
| *delimitacionesGeograficas* | delimitaciones geograficas generadas por el mapa |

##### Devuelve

>   Diccionario

#### def proyecto.asignarEquipos ( *proyecto*, *equipos*)

Funcion que asigna integrantes a un proyecto en base a los integrantes de una
plantilla de equipo.

##### Parámetros

| *proyecto* | instancia del modelo proyecto                    |
|------------|--------------------------------------------------|
| *equipos*  | lista de identificadores de plantillas de equipo |

#### def proyecto.cambioTerritorio ( *request*, *dimensionid*)

recurso de cambio de territorio de dimensiones geograficas y tareas de un
proyecto

##### Parámetros

| *request*     | Instancia HttpRequest                                    |
|---------------|----------------------------------------------------------|
| *dimensionid* | Identificación de la dimensión geografica de un proyecto |

##### Devuelve

>   cadena JSON

#### def proyecto.detalleProyecto ( *request*, *proyid*)

recurso que provee el detalle de un proyecto

##### Parámetros

| *request* | Instancia HttpRequest       |
|-----------|-----------------------------|
| *proyid*  | Identificación del proyecto |

##### Devuelve

>   cadena JSON

#### def proyecto.dimensionesTerritoriales ( *request*, *proyid*)

recurso que provee las dimensiones geograficas de un proyecto

##### Parámetros

| *request* | Instancia HttpRequest       |
|-----------|-----------------------------|
| *proyid*  | Identificación del proyecto |

##### Devuelve

>   cadena JSON

#### def proyecto.eliminarProyecto ( *request*, *proyid*)

recurso de eliminación de proyectos

##### Parámetros

| *request* | Instancia HttpRequest       |
|-----------|-----------------------------|
| *proyid*  | Identificación del proyecto |

##### Devuelve

>   cadena JSON

#### def proyecto.gestionProyectosView ( *request*)

Función que provee una plantilla HTML para la gestión de cambios de un proyecto.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   plantilla HTML

#### def proyecto.listadoProyectos ( *request*)

Recurso de listado de proyectos.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def proyecto.listadoProyectosView ( *request*)

Función que provee una plantilla HTML para la gestión de proyectos.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   plantilla HTML

#### def proyecto.tareasProyectoView ( *request*, *proyid*)

Función que provee una plantilla HTML para la gestión de tareas de un proyecto
especifico.

##### Parámetros

| *request* | Instancia HttpRequest         |
|-----------|-------------------------------|
| *proyid*  | Identificación de un proyecto |

##### Devuelve

>   plantilla HTML

Referencia del Namespace myapp.tareas
-------------------------------------

### Funciones

-   def **listadoTareas** (request)

*recurso que provee el listado de tareas*

-   def **listadoTareasMapa** (request)

*recurso que provee las tareas asociadas a las dimensiónes geograficas del
sistema*

-   def **detalleTarea** (request, tareid)

*recurso que provee el detalle de una tarea*

-   def **almacenamientoTarea** (request)

*recurso de almacenamiento de Tareas*

-   def **eliminarTarea** (request, tareid)

*recurso de eliminación de tareas*

-   def **actualizarTarea** (request, tareid)

*recurso de actualización de tareas*

-   def **validarTarea** (tarea)

*Función que se encarga de validar una tarea especifica.*

-   def **asignacionPuntaje** (userid, tareid, puntaje)

*Funcion que se encarga de aumentar el puntaje actual de un usuario.*

-   def **promoverUsuario** (user)

*Función que promueve un usuario de rol en caso tal cumpla con el puntaje
requerido.*

-   def **notificacionPromocionUsuario** (user, rol)

*Función que envía una notificación via correo a un usuario cuando es promovido
de Rol.*

-   def **tareasXDimensionTerritorial** (request, dimensionid)

*Recurso que provee las tareas que hacen parte de una dimensión geográfica.*

-   def **listadoTareasView** (request)

*Función que provee la plantilla HTML para la gestión de tareas.*

### Documentación de las funciones

#### def tareas.actualizarTarea ( *request*, *tareid*)

recurso de actualización de tareas

##### Parámetros

| *request* | Instancia HttpRequest       |
|-----------|-----------------------------|
| *tareid*  | Identificación de una tarea |

##### Devuelve

>   cadena JSON

#### def tareas.almacenamientoTarea ( *request*)

recurso de almacenamiento de Tareas

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def tareas.asignacionPuntaje ( *userid*, *tareid*, *puntaje*)

Funcion que se encarga de aumentar el puntaje actual de un usuario.

##### Parámetros

| *userid*  | Identificación del usuario               |
|-----------|------------------------------------------|
| *tareid*  | Identificación de una tarea              |
| *puntaje* | puntaje a sumar o restar para un usuario |

#### def tareas.detalleTarea ( *request*, *tareid*)

recurso que provee el detalle de una tarea

##### Parámetros

| *request* | Instancia HttpRequest       |
|-----------|-----------------------------|
| *tareid*  | Identificación de una tarea |

##### Devuelve

>   cadena JSON

#### def tareas.eliminarTarea ( *request*, *tareid*)

recurso de eliminación de tareas

##### Parámetros

| *request* | Instancia HttpRequest       |
|-----------|-----------------------------|
| *tareid*  | Identificación de una tarea |

##### Devuelve

>   cadena JSON

#### def tareas.listadoTareas ( *request*)

recurso que provee el listado de tareas

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def tareas.listadoTareasMapa ( *request*)

recurso que provee las tareas asociadas a las dimensiónes geograficas del
sistema

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def tareas.listadoTareasView ( *request*)

Función que provee la plantilla HTML para la gestión de tareas.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   plantilla HTML

#### def tareas.notificacionPromocionUsuario ( *user*, *rol*)

Función que envía una notificación via correo a un usuario cuando es promovido
de Rol.

##### Parámetros

| *user* | Instancia del modelo Usuario     |
|--------|----------------------------------|
| *rol*  | Nombre del nuevo rol del usuario |

#### def tareas.promoverUsuario ( *user*)

Función que promueve un usuario de rol en caso tal cumpla con el puntaje
requerido.

##### Parámetros

| *user* | Instancia del modelo Usuario |
|--------|------------------------------|


#### def tareas.tareasXDimensionTerritorial ( *request*, *dimensionid*)

Recurso que provee las tareas que hacen parte de una dimensión geográfica.

##### Parámetros

| *request*     | Instancia HttpRequest                     |
|---------------|-------------------------------------------|
| *dimensionid* | Identificación de la dimensión geográfica |

#### def tareas.validarTarea ( *tarea*)

Función que se encarga de validar una tarea especifica.

##### Parámetros

| *tarea* | Instancia del modelo Tarea |
|---------|----------------------------|


##### Devuelve

>   Booleano

Referencia del Namespace myapp.tiposProyecto
--------------------------------------------

### Funciones

-   def **listadoTiposProyecto** (request)

*Recurso que provee el listado de Tipos de proyecto disponibles.*

-   def **almacenamientoTiposProyecto** (request)

*Recurso de almacenamiento de Tipos de proyecto.*

-   def **edicionTipoProyecto** (request, tiproid)

*Recurso de actualización de Tipos de proyecto.*

-   def **eliminarTipoProyecto** (request, tiproid)

*Recurso de eliminación de Tipos de proyecto.*

-   def **tiposProyectoView** (request)

*Función que provee una plantilla HTML para gestión de Tipos de proyecto.*

### Documentación de las funciones

#### def tiposProyecto.almacenamientoTiposProyecto ( *request*)

Recurso de almacenamiento de Tipos de proyecto.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def tiposProyecto.edicionTipoProyecto ( *request*, *tiproid*)

Recurso de actualización de Tipos de proyecto.

##### Parámetros

| *request* | Instancia HttpRequest               |
|-----------|-------------------------------------|
| *tiproid* | Identificación del tipo de proyecto |

##### Devuelve

>   cadena JSON

#### def tiposProyecto.eliminarTipoProyecto ( *request*, *tiproid*)

Recurso de eliminación de Tipos de proyecto.

##### Parámetros

| *request* | Instancia HttpRequest               |
|-----------|-------------------------------------|
| *tiproid* | Identificación del tipo de proyecto |

##### Devuelve

>   cadena JSON

#### def tiposProyecto.listadoTiposProyecto ( *request*)

Recurso que provee el listado de Tipos de proyecto disponibles.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def tiposProyecto.tiposProyectoView ( *request*)

Función que provee una plantilla HTML para gestión de Tipos de proyecto.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   plantilla HTML

Referencia del Namespace myapp.utilidades
-----------------------------------------

### Funciones

-   def **dictfetchall** (cursor)

*Función que formatea el resultado de una consulta de base de datos.*

-   def **listadoGeneros** (request)

*Recurso que provee el listado de los géneros del sistema.*

-   def **listadoNivelesEducativos** (request)

*Recurso que provee el listado de niveles educativos del sistema.*

-   def **listadoBarrios** (request)

*Recurso que provee el listado de barrios de Santiago de Cali.*

-   def **usuarioAutenticado** (request)

*Función que provee la instancia del modelo usuario en base al Token de sesión.*

-   def **obtenerParametroSistema** (parametro)

*Función que provee un parametro del sistema.*

-   def **obtenerEmailsEquipo** (proyid)

*Función que provee el listado de correos electrónicos de los integrantes de un
proyecto.*

-   def **obtenerEmailUsuario** (userid)

*Recurso que provee el correo electrónico de un usuario.*

-   def **notFoundPage** (request, exception=None)

*Función que retorna una plantilla HTML cuando no se encuentra un recurso en el
sistema.*

-   def **serverErrorPage** (request, exception=None)

*Función que retorna una plantilla HTML cuando ocurre un error en el sistema.*

-   def **reporteEstadoProyecto** (proyid)

*Función que calcula el estado actual de un proyecto.*

### Documentación de las funciones

#### def utilidades.dictfetchall ( *cursor*)

Función que formatea el resultado de una consulta de base de datos.

##### Parámetros

| *cursor* | Cursor que contiene el resultado de la consulta |
|----------|-------------------------------------------------|


##### Devuelve

>   lista de diccionarios

#### def utilidades.listadoBarrios ( *request*)

Recurso que provee el listado de barrios de Santiago de Cali.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def utilidades.listadoGeneros ( *request*)

Recurso que provee el listado de los géneros del sistema.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def utilidades.listadoNivelesEducativos ( *request*)

Recurso que provee el listado de niveles educativos del sistema.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   cadena JSON

#### def utilidades.notFoundPage ( *request*, *exception* = None)

Función que retorna una plantilla HTML cuando no se encuentra un recurso en el
sistema.

##### Parámetros

| *request*   | Instancia HttpRequest |
|-------------|-----------------------|
| *exception* | excepción opcional    |

##### Devuelve

>   plantilla HTML

#### def utilidades.obtenerEmailsEquipo ( *proyid*)

Función que provee el listado de correos electrónicos de los integrantes de un
proyecto.

##### Parámetros

| *proyid* | Identificación de un proyecto |
|----------|-------------------------------|


##### Devuelve

>   Lista

#### def utilidades.obtenerEmailUsuario ( *userid*)

Recurso que provee el correo electrónico de un usuario.

##### Parámetros

| *userid* | Identificación de un usuario |
|----------|------------------------------|


##### Devuelve

>   cadena que contiene el correo electrónico del usuario

#### def utilidades.obtenerParametroSistema ( *parametro*)

Función que provee un parametro del sistema.

##### Parámetros

| *parametro* | Identificación del parametro |
|-------------|------------------------------|


##### Devuelve

>   cadena con el valor de parámetro del sistema

#### def utilidades.reporteEstadoProyecto ( *proyid*)

Función que calcula el estado actual de un proyecto.

>   provee datos como: Avance de la ejecución Avance de la validación Cantidad
>   de integrantes

##### Parámetros

| *proyid* | Identificación del proyecto |
|----------|-----------------------------|


##### Devuelve

>   Diccionario

#### def utilidades.serverErrorPage ( *request*, *exception* = None)

Función que retorna una plantilla HTML cuando ocurre un error en el sistema.

##### Parámetros

| *request*   | Instancia HttpRequest |
|-------------|-----------------------|
| *exception* | excepcion opcional    |

##### Devuelve

>   plantilla HTML

#### def utilidades.usuarioAutenticado ( *request*)

Función que provee la instancia del modelo usuario en base al Token de sesión.

##### Parámetros

| *request* | Instancia HttpRequest |
|-----------|-----------------------|


##### Devuelve

>   instancia del modelo Usuario

Documentación de las clases
===========================

Referencia de la Clase myapp.models.Accion
------------------------------------------

Modelo de Permisos del Sistema.

Herencias Model.

### Clases

-   class **Meta**

### Atributos públicos estáticos

-   **accionid** = models.UUIDField(primary_key= True, default = uuid.uuid4(),
    editable = False)

-   **nombre** = models.CharField(max_length = 255)

-   **descripcion** = models.CharField(max_length = 1000)

### Descripción detallada

Modelo de Permisos del Sistema.

### Documentación de los datos miembro

#### myapp.models.Accion.accionid = models.UUIDField(primary_key= True, default = uuid.uuid4(), editable = False)[static]

#### myapp.models.Accion.descripcion = models.CharField(max_length = 1000)[static]

#### myapp.models.Accion.nombre = models.CharField(max_length = 255)[static]

Referencia de la Clase myapp.models.AsignacionPuntaje
-----------------------------------------------------

Modelo de historial de asignaciones de puntaje.

Herencias Model.

### Clases

-   class **Meta**

### Atributos públicos estáticos

-   **asigid** = models.UUIDField(default = uuid.uuid4, primary_key=True)

-   **userid** = models.UUIDField()

-   **tareid** = models.UUIDField()

-   **puntaje** = models.IntegerField()

### Descripción detallada

Modelo de historial de asignaciones de puntaje.

### Documentación de los datos miembro

#### myapp.models.AsignacionPuntaje.asigid = models.UUIDField(default = uuid.uuid4, primary_key=True)[static]

#### myapp.models.AsignacionPuntaje.puntaje = models.IntegerField()[static]

#### myapp.models.AsignacionPuntaje.tareid = models.UUIDField()[static]

#### myapp.models.AsignacionPuntaje.userid = models.UUIDField()[static]

Referencia de la Clase myapp.models.Barrio
------------------------------------------

Modelo de barrios.

Herencias Model.

### Clases

-   class **Meta**

### Atributos públicos estáticos

-   **barrioid** = models.IntegerField(editable=False, primary_key=True)

-   **nombre** = models.CharField(max_length=100)

### Descripción detallada

Modelo de barrios.

### Documentación de los datos miembro

#### myapp.models.Barrio.barrioid = models.IntegerField(editable=False, primary_key=True)[static]

#### myapp.models.Barrio.nombre = models.CharField(max_length=100)[static]

Referencia de la Clase myapp.models.Cartografia
-----------------------------------------------

Modelo de cartografias.

Herencias Model.

### Clases

-   class **Meta**

### Atributos públicos estáticos

-   **cartografiaid** = models.UUIDField(default=uuid.uuid4, editable=False,
    primary_key=True)

-   **instrid** = models.UUIDField()

-   **osmid** = models.CharField(max_length=255)

-   **elemosmid** = models.UUIDField()

-   **userid** = models.UUIDField()

-   **estado** = models.IntegerField(default=0)

-   **tareid** = models.UUIDField()

### Descripción detallada

Modelo de cartografias.

### Documentación de los datos miembro

#### myapp.models.Cartografia.cartografiaid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)[static]

#### myapp.models.Cartografia.elemosmid = models.UUIDField()[static]

#### myapp.models.Cartografia.estado = models.IntegerField(default=0)[static]

#### myapp.models.Cartografia.instrid = models.UUIDField()[static]

#### myapp.models.Cartografia.osmid = models.CharField(max_length=255)[static]

#### myapp.models.Cartografia.tareid = models.UUIDField()[static]

#### myapp.models.Cartografia.userid = models.UUIDField()[static]

Referencia de la Clase myapp.models.Conflictividad
--------------------------------------------------

Modelo de Conflictividades.

Herencias Model.

### Clases

-   class **Meta**

### Atributos públicos estáticos

-   **confid** = models.UUIDField(default=uuid.uuid4, editable=False,
    primary_key=True)

-   **nombre** = models.CharField(max_length=50)

### Descripción detallada

Modelo de Conflictividades.

### Documentación de los datos miembro

#### myapp.models.Conflictividad.confid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)[static]

#### myapp.models.Conflictividad.nombre = models.CharField(max_length=50)[static]

Referencia de la Clase myapp.models.Contexto
--------------------------------------------

Modelo de Contextos.

Herencias Model.

### Clases

-   class **Meta**

### Atributos públicos estáticos

-   **contextoid** = models.UUIDField(primary_key = True, default = uuid.uuid4,
    editable = False)

-   **descripcion** = models.CharField(max_length = 1000)

### Descripción detallada

Modelo de Contextos.

### Documentación de los datos miembro

#### myapp.models.Contexto.contextoid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)[static]

#### myapp.models.Contexto.descripcion = models.CharField(max_length = 1000)[static]

Referencia de la Clase myapp.models.ContextoProyecto
----------------------------------------------------

Modelo de Contextos **Proyecto**.

Herencias Model.

### Clases

-   class **Meta**

### Atributos públicos estáticos

-   **contproyid** = models.UUIDField(primary_key = True, default = uuid.uuid4,
    editable = False)

-   **proyid** = models.UUIDField()

-   **contextoid** = models.UUIDField()

### Descripción detallada

Modelo de Contextos **Proyecto**.

### Documentación de los datos miembro

#### myapp.models.ContextoProyecto.contextoid = models.UUIDField()[static]

#### myapp.models.ContextoProyecto.contproyid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)[static]

#### myapp.models.ContextoProyecto.proyid = models.UUIDField()[static]

Referencia de la Clase myapp.models.Contextualizacion
-----------------------------------------------------

Modelo de los hechos asociados a las conflictividades.

Herencias Model.

### Clases

-   class **Meta**

### Atributos públicos estáticos

-   **contxtid** = models.UUIDField(default=uuid.uuid4, editable=False,
    primary_key=True)

-   **fecha_hecho** = models.DateField()

-   **hora_hecho** = models.TimeField()

-   **dia** = models.IntegerField()

-   **confid** = models.UUIDField()

-   **generoid** = models.UUIDField()

-   **edad** = models.IntegerField()

-   **nivelid** = models.UUIDField()

-   **nombre_barrio** = models.CharField(max_length=300)

-   **cantidad** = models.IntegerField()

-   **barrioid** = models.IntegerField()

### Descripción detallada

Modelo de los hechos asociados a las conflictividades.

### Documentación de los datos miembro

#### myapp.models.Contextualizacion.barrioid = models.IntegerField()[static]

#### myapp.models.Contextualizacion.cantidad = models.IntegerField()[static]

#### myapp.models.Contextualizacion.confid = models.UUIDField()[static]

#### myapp.models.Contextualizacion.contxtid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)[static]

#### myapp.models.Contextualizacion.dia = models.IntegerField()[static]

#### myapp.models.Contextualizacion.edad = models.IntegerField()[static]

#### myapp.models.Contextualizacion.fecha_hecho = models.DateField()[static]

#### myapp.models.Contextualizacion.generoid = models.UUIDField()[static]

#### myapp.models.Contextualizacion.hora_hecho = models.TimeField()[static]

#### myapp.models.Contextualizacion.nivelid = models.UUIDField()[static]

#### myapp.models.Contextualizacion.nombre_barrio = models.CharField(max_length=300)[static]

Referencia de la Clase cors.CorsMiddleware
------------------------------------------

Middleware que se encarga de agregar las cabeceras CORS con el fin de permitir
que el API REST sea consumida desde cualquier fuente.

Herencias object.

### Métodos públicos

-   def **\__init_\_** (self, **get_response**)

-   def **\__call_\_** (self, request)

### Atributos públicos

-   **get_response**

### Descripción detallada

Middleware que se encarga de agregar las cabeceras CORS con el fin de permitir
que el API REST sea consumida desde cualquier fuente.

### Documentación del constructor y destructor

#### def cors.CorsMiddleware.__init_\_ ( *self*, *get_response*)

### Documentación de las funciones miembro

#### def cors.CorsMiddleware.__call_\_ ( *self*, *request*)

### Documentación de los datos miembro

#### cors.CorsMiddleware.get_response

Referencia de la Clase myapp.models.DatosContexto
-------------------------------------------------

Modelo de Datos de **Contexto**.

Herencias Model.

### Clases

-   class **Meta**

### Atributos públicos estáticos

-   **dataid** = models.UUIDField(primary_key = True, default = uuid.uuid4,
    editable = False)

-   **hdxtag** = models.CharField(max_length = 100)

-   **datavalor** = models.CharField(max_length = 100)

-   **datatipe** = models.CharField(max_length=100)

-   **contextoid** = models.UUIDField()

-   **descripcion** = models.CharField(max_length=500)

-   **geojson** = models.CharField(max_length=3000)

-   **fecha** = models.DateField(null=True, blank=True)

-   **hora** = models.TimeField(null=True, blank=True)

### Descripción detallada

Modelo de Datos de **Contexto**.

### Documentación de los datos miembro

#### myapp.models.DatosContexto.contextoid = models.UUIDField()[static]

#### myapp.models.DatosContexto.dataid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)[static]

#### myapp.models.DatosContexto.datatipe = models.CharField(max_length=100)[static]

#### myapp.models.DatosContexto.datavalor = models.CharField(max_length = 100)[static]

#### myapp.models.DatosContexto.descripcion = models.CharField(max_length=500)[static]

#### myapp.models.DatosContexto.fecha = models.DateField(null=True, blank=True)[static]

#### myapp.models.DatosContexto.geojson = models.CharField(max_length=3000)[static]

#### myapp.models.DatosContexto.hdxtag = models.CharField(max_length = 100)[static]

#### myapp.models.DatosContexto.hora = models.TimeField(null=True, blank=True)[static]

Referencia de la Clase myapp.models.Decision
--------------------------------------------

Modelo de Decisiones.

Herencias Model.

### Clases

-   class **Meta**

### Atributos públicos estáticos

-   **desiid** = models.UUIDField(primary_key = True, default = uuid.uuid4,
    editable = False)

-   **desidescripcion** = models.CharField(max_length = 1000)

-   **userid** = models.UUIDField()

### Descripción detallada

Modelo de Decisiones.

### Documentación de los datos miembro

#### myapp.models.Decision.desidescripcion = models.CharField(max_length = 1000)[static]

#### myapp.models.Decision.desiid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)[static]

#### myapp.models.Decision.userid = models.UUIDField()[static]

Referencia de la Clase myapp.models.DecisionProyecto
----------------------------------------------------

Modelo de Decisiones **Proyecto**.

Herencias Model.

### Clases

-   class **Meta**

### Atributos públicos estáticos

-   **desproid** = models.UUIDField(primary_key = True, default = uuid.uuid4,
    editable = False)

-   **proyid** = models.UUIDField()

-   **desiid** = models.UUIDField()

### Descripción detallada

Modelo de Decisiones **Proyecto**.

### Documentación de los datos miembro

#### myapp.models.DecisionProyecto.desiid = models.UUIDField()[static]

#### myapp.models.DecisionProyecto.desproid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)[static]

#### myapp.models.DecisionProyecto.proyid = models.UUIDField()[static]

Referencia de la Clase myapp.models.DelimitacionGeografica
----------------------------------------------------------

Modelo de Dimensiones Geográficas.

Herencias Model.

### Clases

-   class **Meta**

### Atributos públicos estáticos

-   **dimensionid** = models.UUIDField(primary_key=True, default=uuid.uuid4,
    editable=False)

-   **proyid** = models.UUIDField()

-   **nombre** = models.CharField(max_length=255)

-   **geojson** = models.CharField(max_length=1000)

-   **estado** = models.IntegerField(default=1)

### Descripción detallada

Modelo de Dimensiones Geográficas.

### Documentación de los datos miembro

#### myapp.models.DelimitacionGeografica.dimensionid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)[static]

#### myapp.models.DelimitacionGeografica.estado = models.IntegerField(default=1)[static]

#### myapp.models.DelimitacionGeografica.geojson = models.CharField(max_length=1000)[static]

#### myapp.models.DelimitacionGeografica.nombre = models.CharField(max_length=255)[static]

#### myapp.models.DelimitacionGeografica.proyid = models.UUIDField()[static]

Referencia de la Clase myapp.models.ElementoOsm
-----------------------------------------------

Modelo de elementos de Open Street Maps.

Herencias Model.

### Clases

-   class **Meta**

### Atributos públicos estáticos

-   **elemosmid** = models.UUIDField(editable=False, primary_key=True)

-   **nombre** = models.CharField(max_length=255)

-   **llaveosm** = models.CharField(max_length=255)

-   **valorosm** = models.CharField(max_length=255)

-   **closed_way** = models.IntegerField()

### Descripción detallada

Modelo de elementos de Open Street Maps.

### Documentación de los datos miembro

#### myapp.models.ElementoOsm.closed_way = models.IntegerField()[static]

#### myapp.models.ElementoOsm.elemosmid = models.UUIDField(editable=False, primary_key=True)[static]

#### myapp.models.ElementoOsm.llaveosm = models.CharField(max_length=255)[static]

#### myapp.models.ElementoOsm.nombre = models.CharField(max_length=255)[static]

#### myapp.models.ElementoOsm.valorosm = models.CharField(max_length=255)[static]

Referencia de la Clase myapp.models.Encuesta
--------------------------------------------

Modelo de Encuestas.

Herencias Model.

### Clases

-   class **Meta**

### Atributos públicos estáticos

-   **encuestaid** = models.UUIDField(default=uuid.uuid4, editable=False,
    primary_key=True)

-   **instrid** = models.UUIDField()

-   **koboid** = models.UUIDField()

-   **contenido** = models.CharField(max_length=5000)

-   **estado** = models.IntegerField(default=0)

-   **observacion** = models.CharField(blank=True, max_length=3000, null=True)

-   **userid** = models.UUIDField()

-   **tareid** = models.UUIDField()

### Descripción detallada

Modelo de Encuestas.

### Documentación de los datos miembro

#### myapp.models.Encuesta.contenido = models.CharField(max_length=5000)[static]

#### myapp.models.Encuesta.encuestaid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)[static]

#### myapp.models.Encuesta.estado = models.IntegerField(default=0)[static]

#### myapp.models.Encuesta.instrid = models.UUIDField()[static]

#### myapp.models.Encuesta.koboid = models.UUIDField()[static]

#### myapp.models.Encuesta.observacion = models.CharField(blank=True, max_length=3000, null=True)[static]

#### myapp.models.Encuesta.tareid = models.UUIDField()[static]

#### myapp.models.Encuesta.userid = models.UUIDField()[static]

Referencia de la Clase myapp.models.Equipo
------------------------------------------

Modelo de Equipos.

Herencias Model.

### Clases

-   class **Meta**

### Atributos públicos estáticos

-   **equid** = models.UUIDField(primary_key = True, default = uuid.uuid4,
    editable = False)

-   **userid** = models.UUIDField()

-   **proyid** = models.UUIDField()

-   **miembroestado** = models.IntegerField(default=1)

### Descripción detallada

Modelo de Equipos.

### Documentación de los datos miembro

#### myapp.models.Equipo.equid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)[static]

#### myapp.models.Equipo.miembroestado = models.IntegerField(default=1)[static]

#### myapp.models.Equipo.proyid = models.UUIDField()[static]

#### myapp.models.Equipo.userid = models.UUIDField()[static]

Referencia de la Clase myapp.models.FuncionRol
----------------------------------------------

Modelo de permisos para los roles.

Herencias Model.

### Clases

-   class **Meta**

### Atributos públicos estáticos

-   **funcrolid** = models.UUIDField(primary_key = True, default = uuid.uuid4,
    editable = False)

-   **rolid** = models.UUIDField()

-   **accionid** = models.CharField(max_length = 255)

-   **funcrolestado** = models.IntegerField()

-   **funcrolpermiso** = models.IntegerField()

### Descripción detallada

Modelo de permisos para los roles.

### Documentación de los datos miembro

#### myapp.models.FuncionRol.accionid = models.CharField(max_length = 255)[static]

#### myapp.models.FuncionRol.funcrolestado = models.IntegerField()[static]

#### myapp.models.FuncionRol.funcrolid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)[static]

#### myapp.models.FuncionRol.funcrolpermiso = models.IntegerField()[static]

#### myapp.models.FuncionRol.rolid = models.UUIDField()[static]

Referencia de la Clase myapp.models.Genero
------------------------------------------

Modelo de Generos.

### Clases

-   class **Meta**

### Atributos públicos estáticos

-   **generoid** = models.UUIDField(primary_key=True, default=uuid.uuid4,
    editable=False)

-   **nombre** = models.CharField(max_length=100)

### Descripción detallada

Modelo de Generos.

### Documentación de los datos miembro

#### myapp.models.Genero.generoid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)[static]

#### myapp.models.Genero.nombre = models.CharField(max_length=100)[static]

Referencia de la Clase myapp.models.Instrumento
-----------------------------------------------

Modelo de instrumentos.

### Clases

-   class **Meta**

### Atributos públicos estáticos

-   **instrid** = models.UUIDField(primary_key = True, default = uuid.uuid4,
    editable = False)

-   **instridexterno** = models.CharField(max_length = 255)

-   **instrtipo** = models.IntegerField()

-   **instrnombre** = models.CharField(max_length = 255)

-   **instrdescripcion** = models.CharField(max_length = 3000, null = True,
    blank = True)

-   **geojson** = models.CharField(max_length=1000, null = True, blank=True)

### Descripción detallada

Modelo de instrumentos.

### Documentación de los datos miembro

#### myapp.models.Instrumento.geojson = models.CharField(max_length=1000, null = True, blank=True)[static]

#### myapp.models.Instrumento.instrdescripcion = models.CharField(max_length = 3000, null = True, blank = True)[static]

#### myapp.models.Instrumento.instrid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)[static]

#### myapp.models.Instrumento.instridexterno = models.CharField(max_length = 255)[static]

#### myapp.models.Instrumento.instrnombre = models.CharField(max_length = 255)[static]

#### myapp.models.Instrumento.instrtipo = models.IntegerField()[static

Referencia de la Clase myapp.models.MiembroPlantilla
----------------------------------------------------

Modelo de miembros de plantilla.

Herencias Model.

### Clases

-   class **Meta**

### Atributos públicos estáticos

-   **miplid** = models.UUIDField(default=uuid.uuid4, primary_key=True)

-   **userid** = models.UUIDField()

-   **estado** = models.IntegerField(default=1)

-   **planid** = models.UUIDField()

### Descripción detallada

Modelo de miembros de plantilla.

### Documentación de los datos miembro

#### myapp.models.MiembroPlantilla.estado = models.IntegerField(default=1)[static]

#### myapp.models.MiembroPlantilla.miplid = models.UUIDField(default=uuid.uuid4, primary_key=True)[static]

#### myapp.models.MiembroPlantilla.planid = models.UUIDField()[static]

#### myapp.models.MiembroPlantilla.userid = models.UUIDField()[static]

Referencia de la Clase myapp.models.NivelEducativo
--------------------------------------------------

Modelo de Niveles educativos.

Herencias Model.

### Clases

-   class **Meta**

### Atributos públicos estáticos

-   **nivelid** = models.UUIDField(primary_key=True, default=uuid.uuid4,
    editable=False)

-   **nombre** = models.CharField(max_length=100)

### Descripción detallada

Modelo de Niveles educativos.

### Documentación de los datos miembro

#### myapp.models.NivelEducativo.nivelid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)[static]

#### myapp.models.NivelEducativo.nombre = models.CharField(max_length=100)[static]

#### La documentación para esta clase fue generada a partir del siguiente fichero:

-   C:/Users/Usuario.DESKTOP-7RP0F57/Documents/kevin/proyectos/projects-ubuntu-bionic/opc/opc-web/myapp/**models.py**

Referencia de la Clase myapp.models.Parametro
---------------------------------------------

Modelo de parámetros del sistema.

Herencias Model.

### Clases

-   class **Meta**

### Atributos públicos estáticos

-   **paramid** = models.CharField(max_length=1000, primary_key=True)

-   **paramvalor** = models.CharField(max_length=1000)

-   **paramdesc** = models.CharField(max_length=1000)

### Descripción detallada

Modelo de parámetros del sistema.

### Documentación de los datos miembro

#### myapp.models.Parametro.paramdesc = models.CharField(max_length=1000)[static]

#### myapp.models.Parametro.paramid = models.CharField(max_length=1000, primary_key=True)[static]

#### myapp.models.Parametro.paramvalor = models.CharField(max_length=1000)[static]

#### La documentación para esta clase fue generada a partir del siguiente fichero:

-   C:/Users/Usuario.DESKTOP-7RP0F57/Documents/kevin/proyectos/projects-ubuntu-bionic/opc/opc-web/myapp/**models.py**

Referencia de la Clase myapp.models.PlantillaEquipo
---------------------------------------------------

Modelo de plantillas de equipo.

Herencias Model.

### Clases

-   class **Meta**

### Atributos públicos estáticos

-   **planid** = models.UUIDField(default=uuid.uuid4, primary_key=True)

-   **descripcion** = models.TextField()

-   **userid** = models.UUIDField()

### Descripción detallada

Modelo de plantillas de equipo.

### Documentación de los datos miembro

#### myapp.models.PlantillaEquipo.descripcion = models.TextField()[static]

#### myapp.models.PlantillaEquipo.planid = models.UUIDField(default=uuid.uuid4, primary_key=True)[static]

#### myapp.models.PlantillaEquipo.userid = models.UUIDField()[static]

#### La documentación para esta clase fue generada a partir del siguiente fichero:

-   C:/Users/Usuario.DESKTOP-7RP0F57/Documents/kevin/proyectos/projects-ubuntu-bionic/opc/opc-web/myapp/**models.py**

Referencia de la Clase myapp.models.Proyecto
--------------------------------------------

Modelo de Proyectos.

Herencias Model.

### Clases

-   class **Meta**

### Atributos públicos estáticos

-   **proyid** = models.UUIDField(primary_key = True, default = uuid.uuid4,
    editable = False)

-   **proynombre** = models.CharField(max_length = 255)

-   **proydescripcion** = models.CharField(max_length = 1000)

-   **proyidexterno** = models.CharField(max_length = 255)

-   **proyfechacreacion** = models.CharField(max_length=100)

-   **proyfechacierre** = models.DateField(null=True, blank=True)

-   **proyestado** = models.IntegerField()

-   **proypropietario** = models.UUIDField()

-   **proyfechainicio** = models.DateField(null=True, blank=True)

-   **tiproid** = models.UUIDField()

### Descripción detallada

Modelo de Proyectos.

### Documentación de los datos miembro

#### myapp.models.Proyecto.proydescripcion = models.CharField(max_length = 1000)[static]

#### myapp.models.Proyecto.proyestado = models.IntegerField()[static]

#### myapp.models.Proyecto.proyfechacierre = models.DateField(null=True, blank=True)[static]

#### myapp.models.Proyecto.proyfechacreacion = models.CharField(max_length=100)[static]

#### myapp.models.Proyecto.proyfechainicio = models.DateField(null=True, blank=True)[static]

#### myapp.models.Proyecto.proyid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)[static]

#### myapp.models.Proyecto.proyidexterno = models.CharField(max_length = 255)[static]

#### myapp.models.Proyecto.proynombre = models.CharField(max_length = 255)[static]

#### myapp.models.Proyecto.proypropietario = models.UUIDField()[static]

#### myapp.models.Proyecto.tiproid = models.UUIDField()[static]

#### La documentación para esta clase fue generada a partir del siguiente fichero:

-   C:/Users/Usuario.DESKTOP-7RP0F57/Documents/kevin/proyectos/projects-ubuntu-bionic/opc/opc-web/myapp/**models.py**

Referencia de la Clase myapp.models.Rol
---------------------------------------

Modelo de Roles del sistema.

Herencias Model.

### Clases

-   class **Meta**

### Atributos públicos estáticos

-   **rolid** = models.UUIDField(primary_key = True, default = uuid.uuid4,
    editable = False)

-   **rolname** = models.CharField(max_length=50)

-   **roldescripcion** = models.CharField(max_length = 255)

-   **rolestado** = models.IntegerField()

### Descripción detallada

Modelo de Roles del sistema.

### Documentación de los datos miembro

#### myapp.models.Rol.roldescripcion = models.CharField(max_length = 255)[static]

#### myapp.models.Rol.rolestado = models.IntegerField()[static]

#### myapp.models.Rol.rolid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)[static]

#### myapp.models.Rol.rolname = models.CharField(max_length=50)[static]

#### La documentación para esta clase fue generada a partir del siguiente fichero:

-   C:/Users/Usuario.DESKTOP-7RP0F57/Documents/kevin/proyectos/projects-ubuntu-bionic/opc/opc-web/myapp/**models.py**

Referencia de la Clase myapp.models.Tarea
-----------------------------------------

Modelo de Tareas.

Herencias Model.

### Clases

-   class **Meta**

### Atributos públicos estáticos

-   **tareid** = models.UUIDField(primary_key = True, default = uuid.uuid4,
    editable = False)

-   **tarenombre** = models.CharField(max_length = 255)

-   **taretipo** = models.IntegerField()

-   **tarerestricgeo** = models.CharField(max_length = 1000)

-   **tarerestriccant** = models.IntegerField()

-   **tarerestrictime** = models.CharField(max_length = 1000)

-   **instrid** = models.UUIDField()

-   **proyid** = models.UUIDField()

-   **dimensionid** = models.UUIDField(null=True, blank=True)

-   **geojson_subconjunto** = models.CharField(max_length=1000)

-   **tarefechacreacion** = models.DateTimeField(null = True, blank = True,
    default=datetime.today())

-   **taredescripcion** = models.CharField(max_length=1000)

-   **tareestado** = models.IntegerField(default=0)

-   **observaciones** = models.TextField(blank = True, null = True)

### Descripción detallada

Modelo de Tareas.

### Documentación de los datos miembro

#### myapp.models.Tarea.dimensionid = models.UUIDField(null=True, blank=True)[static]

#### myapp.models.Tarea.geojson_subconjunto = models.CharField(max_length=1000)[static]

#### myapp.models.Tarea.instrid = models.UUIDField()[static]

#### myapp.models.Tarea.observaciones = models.TextField(blank = True, null = True)[static]

#### myapp.models.Tarea.proyid = models.UUIDField()[static]

#### myapp.models.Tarea.taredescripcion = models.CharField(max_length=1000)[static]

#### myapp.models.Tarea.tareestado = models.IntegerField(default=0)[static]

#### myapp.models.Tarea.tarefechacreacion = models.DateTimeField(null = True, blank = True, default=datetime.today())[static]

#### myapp.models.Tarea.tareid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)[static]

#### myapp.models.Tarea.tarenombre = models.CharField(max_length = 255)[static]

#### myapp.models.Tarea.tarerestriccant = models.IntegerField()[static]

#### myapp.models.Tarea.tarerestricgeo = models.CharField(max_length = 1000)[static]

#### myapp.models.Tarea.tarerestrictime = models.CharField(max_length = 1000)[static]

#### myapp.models.Tarea.taretipo = models.IntegerField()[static]

#### La documentación para esta clase fue generada a partir del siguiente fichero:

-   C:/Users/Usuario.DESKTOP-7RP0F57/Documents/kevin/proyectos/projects-ubuntu-bionic/opc/opc-web/myapp/**models.py**

Referencia de la Clase myapp.models.TipoProyecto
------------------------------------------------

Modelo de Tipos de **Proyecto**.

Herencias Model.

### Clases

-   class **Meta**

### Atributos públicos estáticos

-   **tiproid** = models.UUIDField(default = uuid.uuid4, primary_key=True)

-   **nombre** = models.CharField(max_length=100)

-   **descripcion** = models.TextField()

### Descripción detallada

Modelo de Tipos de **Proyecto**.

### Documentación de los datos miembro

#### myapp.models.TipoProyecto.descripcion = models.TextField()[static]

#### myapp.models.TipoProyecto.nombre = models.CharField(max_length=100)[static]

#### myapp.models.TipoProyecto.tiproid = models.UUIDField(default = uuid.uuid4, primary_key=True)[static]

#### La documentación para esta clase fue generada a partir del siguiente fichero:

-   C:/Users/Usuario.DESKTOP-7RP0F57/Documents/kevin/proyectos/projects-ubuntu-bionic/opc/opc-web/myapp/**models.py**

Referencia de la Clase myapp.models.Usuario
-------------------------------------------

Modelo de usuario.

Herencias AbstractBaseUser.

### Clases

-   class **Meta**

### Atributos públicos estáticos

-   **userid** = models.UUIDField(primary_key = True, default = uuid.uuid4,
    editable = False)

-   **useremail** = models.EmailField(max_length = 255, unique=True)

-   **password** = models.CharField(max_length = 255)

-   **usertoken** = models.CharField(max_length = 255, null = True, blank =
    True)

-   **userfullname** = models.CharField(max_length = 255)

-   **rolid** = models.UUIDField()

-   **userleveltype** = models.IntegerField()

-   **userestado** = models.IntegerField()

-   **fecha_nacimiento** = models.DateField()

-   **generoid** = models.UUIDField()

-   **barrioid** = models.IntegerField()

-   **nivel_educativo_id** = models.UUIDField()

-   **telefono** = models.CharField(max_length=20)

-   **latitud** = models.CharField(blank=True, null=True, max_length=30)

-   **longitud** = models.CharField(blank=True, null=True, max_length=30)

-   **horaubicacion** = models.CharField(blank=True, null=True, max_length=100)

-   **puntaje** = models.IntegerField(null=True, blank=True, default=0)

-   **objects** = **MyUserManager**()

-   string **USERNAME_FIELD** = "useremail"

### Descripción detallada

Modelo de usuario.

### Documentación de los datos miembro

#### myapp.models.Usuario.barrioid = models.IntegerField()[static]

#### myapp.models.Usuario.fecha_nacimiento = models.DateField()[static]

#### myapp.models.Usuario.generoid = models.UUIDField()[static]

#### myapp.models.Usuario.horaubicacion = models.CharField(blank=True, null=True, max_length=100)[static]

#### myapp.models.Usuario.latitud = models.CharField(blank=True, null=True, max_length=30)[static]

#### myapp.models.Usuario.longitud = models.CharField(blank=True, null=True, max_length=30)[static]

#### myapp.models.Usuario.nivel_educativo_id = models.UUIDField()[static]

#### myapp.models.Usuario.objects = MyUserManager()[static]

#### myapp.models.Usuario.password = models.CharField(max_length = 255)[static]

#### myapp.models.Usuario.puntaje = models.IntegerField(null=True, blank=True, default=0)[static]

#### myapp.models.Usuario.rolid = models.UUIDField()[static]

#### myapp.models.Usuario.telefono = models.CharField(max_length=20)[static]

#### myapp.models.Usuario.useremail = models.EmailField(max_length = 255, unique=True)[static]

#### myapp.models.Usuario.userestado = models.IntegerField()[static]

#### myapp.models.Usuario.userfullname = models.CharField(max_length = 255)[static]

#### myapp.models.Usuario.userid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)[static]

#### myapp.models.Usuario.userleveltype = models.IntegerField()[static]

#### string myapp.models.Usuario.USERNAME_FIELD = "useremail"[static]

#### myapp.models.Usuario.usertoken = models.CharField(max_length = 255, null = True, blank = True)[static]
