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

require('./components/permisosRol.js');

//import '../../../node-modules/vue-multiselect/dist/vue-multiselect.min.css';