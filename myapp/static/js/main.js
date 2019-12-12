window.getToken = function(){

    let userInfo = JSON.parse(sessionStorage.getItem('userinfo'));

    if(userInfo != null && typeof userInfo == 'object' && userInfo.hasOwnProperty('token')){


        return 'Bearer ' + userInfo.token;

    } else if(window.location.pathname != '/'){

        return location.href = '/';
    }

}

window.getUser = function(){

    let userInfo = JSON.parse(sessionStorage.getItem('userinfo'));

    if(userInfo != null && typeof userInfo == 'object' && userInfo.hasOwnProperty('user')){


        return userInfo.user;

    } else{

        return location.href = '/';
    }
}

window.logout = function(){


    sessionStorage.removeItem('userinfo');
    location.href = "/";
}

// Vue.js
window.Vue = require('vue');

// Axios
window.axios = require('axios');

// Sweet Alert 2
import Swal from 'sweetalert2';

import Multiselect from 'vue-multiselect';

Vue.component('multiselect', Multiselect);

// Leaflet
require('./plugins/leaflet/leaflet.js');

// Leaflet Draw
require('leaflet-draw/dist/leaflet.draw.js');

// Filtro de estado de las entidades
Vue.filter('estado-entidad', function(value){

    if(value == 1){

        return "Activo";

    } else if(value == 0){

        return "Inactivo";
    }

});

// const webdriver = require('selenium-webdriver');
// const chrome = require('selenium-webdriver/chrome');

// Instancia Vue para Gestión de proyectos
require('./components/proyectos').proyecto;

// Instancia Vue para Gestión de Tareas
require('./components/tareas').tarea;

// Instancia Vue para Gestión de Instrumentos
require('./components/instrumentos').instrumento;

// Instancia Vue para Gestión de Decisiones
require('./components/decisiones').decision;

// Instancia Vue para Gestión de Usuarios
require('./components/usuarios').usuario;

// Instancia Vue para gestión de Roles
require('./components/roles').rol;

// Gestión de Permisos
require('./components/permisosRol.js');

// Gestión de Autenticación
require('./components/login').login;

// Gestión de Contextos
require('./components/contextos').contexto;

// Gestión de Datos de Contexto
require('./components/datosContexto').datoContexto;

// Información de Encuestas
require('./components/informacion-encuesta').informacionEncuesta;

// Recuperación de contraseña
require('./components/passwordReset').passwordReset;

// Equipos de Proyectos
require('./components/equipos').equipo;

// Gestión de proyectos - Proyectista
require('./components/gestion-proyectos-mapa').gestionProyecto;

// Estadisticas
require('./components/estadisticas').estadisticas;

// Gestión de Plantillas de Equipo
require('./components/plantillas/plantillasEquipo').gestionPlantilla;

// Gestión de Miembros de plantillas de equipo
require('./components/plantillas/miembrosPlantilla').miembrosPlantilla;

// Estilos
import './../scss/app/app.scss';