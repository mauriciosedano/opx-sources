"""opc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myapp import views
from myapp.view import (
    auth,
    equipo,
    proyecto,
    tareas,
    utilidades,
    osm,
    contextualizacion,
    estadisticas,
    plantillaEquipo
)

urlpatterns = [
    #path('admin/', admin.site.urls),

    path('', views.loginView),
    path('login/', views.login),

    path('auth/password-reset/', auth.passwordReset),
    path('auth/password-reset-verification/', auth.passwordResetVerification),
    path('auth/password-reset/<str:token>', auth.passwordResetConfirmation),
    path('auth/password-reset-done/', auth.passwordResetDone),

    path('usuarios/', views.listadoUsuariosView),
    path('usuarios/list/', views.listadoUsuarios),
    path('usuarios/store/', views.almacenarUsuario),
    path('usuarios/detail/<str:userid>', views.detalleUsuario),
    path('usuarios/delete/<str:userid>', views.eliminarUsuario),
    path('usuarios/<str:userid>', views.actualizarUsuario),

    path('contextos/', views.listadoContextosView),
    path('contextos/list/', views.listadoContextos),
    path('contextos/store/', views.almacenamientoContexto),
    path('contextos/delete/<str:contextoid>', views.eliminarContexto),
    path('contextos/<str:contextoid>', views.actualizarContexto),
    path('contextos/datos/<str:contextoid>', views.listadoDatosContextoView),

    path('datos-contexto/list/', views.listadoDatosContextoCompleto),
    path('datos-contexto/list/<str:contextoid>', views.listadoDatosContexto),
    path('datos-contexto/store/', views.almacenarDatoContexto),
    path('datos-contexto/delete/<str:dataid>', views.eliminarDatoContexto),
    path('datos-contexto/<str:dataid>', views.actualizarDatoContexto),

    path('decisiones/', views.listadoDecisionesView),
    path('decisiones/list/', views.listadoDecisiones),
    path('decisiones/store/', views.almacenarDecision),
    path('decisiones/delete/<str:desiid>/', views.eliminarDecision),
    path('decisiones/<str:desiid>', views.actualizarDecision),

    path('decisiones-proyecto/', views.listadoDecisionesProyecto),
    path('decisiones-proyecto/store/', proyecto.almacenarDecisionProyecto),
    path('decisiones-proyecto/delete/<str:desproid>/', views.eliminarDecisionProyecto),
    path('decisiones-proyecto/<str:desproid>', views.actualizarDecisionProyecto),

    path('equipos/list/<str:proyid>', equipo.equipoProyecto),
    path('equipos/<str:proyid>/usuarios-disponibles/', equipo.usuariosDisponiblesProyecto),
    path('equipos/store/', equipo.almacenamientoEquipo),
    path('equipos/delete/<str:equid>', equipo.eliminarEquipo),
    path('equipos/proyecto/<str:proyid>', equipo.equipoProyectoView),
    path('equipos/<str:equid>', equipo.actualizarEquipo),

    path('plantillas-equipo/list/', plantillaEquipo.listadoPlantillas),
    path('plantillas-equipo/<str:planid>/delete/', plantillaEquipo.eliminarPlantilla),
    path('plantillas-equipo/store/', plantillaEquipo.crearPlantilla),
    path('plantillas-equipo/<str:planid>', plantillaEquipo.edicionPlantilla),

    path('acciones/list/', views.listadoAcciones),

    path('funciones-rol/list/<str:rolid>', views.listadoFuncionesRol),
    path('funciones-rol/store/', views.almacenamientoFuncionRol),
    path('funciones-rol/delete/<str:funcrolid>', views.eliminarFuncionRol),
    path('funciones-rol/<str:funcrolid>', views.actualizarFuncionRol),

    path('instrumentos/', views.listadoInstrumentosView),
    path('instrumentos/list/', views.listadoInstrumentos),
    path('instrumentos/store/', views.almacenamientoInstrumento),
    path('instrumentos/delete/<str:instrid>', views.eliminarInstrumento),
    path('instrumentos/<str:instrid>', views.actualizarInstrumento),
    path('instrumentos/<str:id>/informacion/', views.informacionInstrumento),
    path('instrumentos/<str:id>/implementar/', views.implementarFormularioKoboToolbox),
    path('instrumentos/<str:id>/verificar-implementacion/', views.verificarImplementaciónFormulario),
    path('instrumentos/encuesta/crear', views.creacionEncuestaView),
    path('instrumentos/formularios-kobotoolbox/list/', views.listadoFormulariosKoboToolbox),
    path('instrumentos/enlace-formulario/<str:tareid>', views.enlaceFormularioKoboToolbox),
    path('instrumentos/mapear/<str:tareid>', osm.AgregarElemento),
    path('instrumentos/detalle-cartografia/<str:tareid>', osm.cartografiasInstrumento),
    path('instrumentos/eliminar-cartografia/<str:cartografiaid>', osm.eliminarCartografia),
    path('instrumentos/revisar-encuesta/<str:encuestaid>', views.revisarEncuesta),

    path('proyectos/', proyecto.listadoProyectosView),
    path('proyectos/gestion/', proyecto.gestionProyectosView),
    path('proyectos/list/', proyecto.listadoProyectos),
    path('proyectos/store/', proyecto.almacenamientoProyecto),
    path('proyectos/delete/<str:proyid>/', proyecto.eliminarProyecto),
    path('proyectos/<str:proyid>', proyecto.actualizarProyecto),
    path('proyectos/detail/<str:proyid>', proyecto.detalleProyecto),
    path('proyectos/dimensiones-territoriales/<str:proyid>', proyecto.dimensionesTerritoriales),
    path('proyectos/<str:proyid>/tareas/', proyecto.tareasProyectoView),

    path('roles/', views.listadoRolesView),
    path('roles/list/', views.listadoRoles),
    path('roles/store/', views.almacenamientoRol),
    path('roles/delete/<str:rolid>', views.eliminarRol),
    path('roles/<str:rolid>', views.actualizarRol),
    path('roles/permisos/<str:rolid>', views.permisosRolView),

    path('tareas/', tareas.listadoTareasView),
    path('tareas/list/', tareas.listadoTareas),
    path('tareas/store/', tareas.almacenamientoTarea),
    path('tareas/delete/<str:tareid>/', tareas.eliminarTarea),
    path('tareas/<str:tareid>', tareas.actualizarTarea),
    path('tareas/datos-geoespaciales/', tareas.listadoTareasMapa),
    path('tareas/detail/<str:tareid>', tareas.detalleTarea),
    path('instrumentos/informacion/<str:id>', views.informacionInstrumentoView),

    path('generos/list/', utilidades.listadoGeneros),
    path('niveles-educativos/list/', utilidades.listadoNivelesEducativos),
    path('elementos-osm/list/', osm.elementosOsm),

    path('barrios/list/', utilidades.listadoBarrios),

    path('contextualizacion/categorizacion/', contextualizacion.categorizacion),
    path('contextualizacion/todo/', contextualizacion.todo),
    path('contextualizacion/mes/', contextualizacion.mensual),
    path('contextualizacion/semana/', contextualizacion.semanal),
    path('contextualizacion/dia/', contextualizacion.dia),

    path('estadisticas/usuarios-x-rol/', estadisticas.usuariosXRol),
    path('estadisticas/cantidad-usuarios/', estadisticas.cantidadUsuarios),
    path('estadisticas/ranking/', estadisticas.ranking),
    path('estadisticas/<str:proyid>/tareas-x-tipo/', estadisticas.tareasXTipo),
    path('estadisticas/<str:proyid>/tareas-x-estado/', estadisticas.tareasXEstado),
    path('estadisticas/proyectos-tareas/', estadisticas.proyectosTareas),
    path('dashboard/', estadisticas.estadisticasView)
]