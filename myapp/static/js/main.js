window.getToken = function(){

    let userInfo = JSON.parse(sessionStorage.getItem('userinfo'));

    if(userInfo != null && typeof userInfo == 'object' && userInfo.hasOwnProperty('token')){


        return 'Bearer ' + userInfo.token;

    } else{

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

// Filtro de estado de las entidades
Vue.filter('estado-entidad', function(value){

    if(value == 1){

        return "Activo";

    } else if(value == 0){

        return "Inactivo";
    }

});

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

require('./components/datosContexto').datoContexto;

//import '../../../node-modules/vue-multiselect/dist/vue-multiselect.min.css';