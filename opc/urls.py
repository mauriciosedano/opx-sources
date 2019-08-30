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

urlpatterns = [
    #path('admin/', admin.site.urls),

    path('usuarios/', views.listadoUsuariosView),
    path('usuarios/list/', views.listadoUsuarios),
    path('usuarios/store/', views.almacenarUsuario),
    path('usuarios/delete/<str:userid>', views.eliminarUsuario),
    path('usuarios/<str:userid>', views.actualizarUsuario),

    path('datos-contexto/', views.listadoDatosContexto),
    path('datos-contexto/store/', views.almacenarDatoContexto),
    path('datos-contexto/delete/<str:dataid>/', views.eliminarDatoContexto),
    path('datos-contexto/<str:dataid>/', views.actualizarDatoContexto),

    path('decisiones/', views.listadoDecisionesView),
    path('decisiones/list/', views.listadoDecisiones),
    path('decisiones/store/', views.almacenarDecision),
    path('decisiones/delete/<str:desiid>/', views.eliminarDecision),
    path('decisiones/<str:desiid>', views.actualizarDecision),

    path('decisiones-proyecto/', views.listadoDecisionesProyecto),
    path('decisiones-proyecto/store/', views.almacenarDecisionProyecto),
    path('decisiones-proyecto/delete/<str:desproid>/', views.eliminarDecisionProyecto),
    path('decisiones-proyecto/<str:desproid>', views.actualizarDecisionProyecto),

    path('equipos/', views.listadoEquipos),
    path('equipos/store/', views.almacenamientoEquipo),
    path('equipos/delete/<str:equid>/', views.eliminarEquipo),
    path('equipos/<str:equid>', views.actualizarEquipo),

    path('funciones-rol/', views.listadoFuncionesRol),
    path('funciones-rol/store/', views.almacenamientoFuncionRol),
    path('funciones-rol/delete/<str:funcrolid>/', views.eliminarFuncionRol),
    path('funciones-rol/<str:funcrolid>', views.actualizarFuncionRol),

    path('instrumentos/', views.listadoInstrumentosView),
    path('instrumentos/list/', views.listadoInstrumentos),
    path('instrumentos/store/', views.almacenamientoInstrumento),
    path('instrumentos/delete/<str:instrid>', views.eliminarInstrumento),
    path('instrumentos/<str:instrid>', views.actualizarInstrumento),

    path('proyectos/', views.listadoProyectosView),
    path('proyectos/list/', views.listadoProyectos),
    path('proyectos/store/', views.almacenamientoProyecto),
    path('proyectos/delete/<str:proyid>/', views.eliminarProyecto),
    path('proyectos/<str:proyid>', views.actualizarProyecto),

    path('roles/list/', views.listadoRoles),
    path('roles/store/', views.almacenamientoRol),
    path('roles/delete/<str:rolid>/', views.eliminarRol),
    path('roles/<str:rolid>', views.actualizarRol),

    path('tareas/', views.listadoTareasView),
    path('tareas/list/', views.listadoTareas),
    path('tareas/store/', views.almacenamientoTarea),
    path('tareas/delete/<str:tareid>/', views.eliminarTarea),
    path('tareas/<str:tareid>', views.actualizarTarea)
]