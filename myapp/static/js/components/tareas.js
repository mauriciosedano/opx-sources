let tarea = new Vue({
    delimiters: ['[[', ']]'],
    el: '#gestion-tareas',
    created(){

        if(window.location.pathname == '/tareas/'){

            this.listadoTareas();
            this.listadoProyectos();
            this.listadoInstrumentos();
        }
    },
    data: {
        tareas: [],
        edicionTarea: {},
        almacenamientoTarea: {},
        proyectos: [],
        instrumentos: [],
        loading: false
    },
    methods: {
        listadoTareas(){

            this.loader(true);

            axios({
                method: 'GET',
                url: '/tareas/list/',
                headers: {
                    Authorization: getToken()
                }
            })
            .then(response => {

                this.loader(false);

                if(response.data.code == 200 && response.data.status == 'success'){

                    this.tareas = response.data.tareas;
                }
            });
        },
        almacenarTarea(){

            this.loader(true);

            var queryString = Object.keys(this.almacenamientoTarea).map(key => {
                return key + '=' + this.almacenamientoTarea[key]
            }).join('&');

            axios({
                method: 'post',
                url: '/tareas/store/',
                data: queryString,
                headers: {
                    'Content-type': 'application/x-www-form-urlencoded',
                    Authorization: getToken()
                }
            })
            .then(response => {

                $("#agregar-tarea").modal('hide')
                this.almacenamientoTarea = {};
                this.listadoTareas();

                this.loader(false);

                Swal.fire({
                  title: 'Exito!',
                  text: 'Tarea creada satisfactoriamente',
                  type: 'success',
                  confirmButtonText: 'Acepto'
                });
            })
            .catch(response => {

                $("#agregar-tarea").modal('hide')
                this.almacenamientoTarea = {};

                this.loader(false);

                Swal.fire({
                  title: 'Error!',
                  text: 'Ocurrio un error. Por favor intenta de nuevo',
                  type: 'error',
                  confirmButtonText: 'Acepto'
                });
            });
        },
        eliminarTarea(id){

            Swal.fire({
              title: 'Estas seguro?',
              text: "No lo puedes revertir",
              type: 'warning',
              showCancelButton: true,
              confirmButtonColor: '#3085d6',
              cancelButtonColor: '#d33',
              confirmButtonText: 'Acepto!'

            }).then((result) => {

              if (result.value) {

                this.loader(true);

                axios({
                    method: 'DELETE',
                    url: '/tareas/delete/' + id,
                    headers: {
                        Authorization: getToken()
                    }
                })
                .then(response => {

                    this.loader(false);

                    this.listadoTareas();

                    Swal.fire(
                      'Eliminado!',
                      'La tarea fue eliminada de forma exitosa',
                      'success'
                    );
                })
                .catch(response => {

                     this.listadoTareas();

                     this.loader(false);

                     Swal.fire(
                      'Error!',
                      'Ocurrio un error por favor intenta de nuevo',
                      'error'
                    );
                });
              }
            });
        },
        editarTarea(){

            this.loader(true);

            var queryString = Object.keys(this.edicionTarea).map(key => {

                let valor = "";

                if(key == 'tarerestricgeo' && typeof this.edicionTarea.tarerestricgeo == 'object'){

                    valor = JSON.stringify(this.edicionTarea.tarerestricgeo);

                } else if(key == 'tarerestrictime' && typeof this.edicionTarea.tarerestrictime == 'object'){

                    valor = JSON.stringify(this.edicionTarea.tarerestrictime);

                } else{

                    valor = this.edicionTarea[key];
                }

                return key + '=' + valor;

            }).join('&');

            axios({
                method: 'post',
                url: '/tareas/' + this.edicionTarea.tareid,
                data: queryString,
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    Authorization: getToken()
                }
            })
            .then(response => {

                $("#editar-tarea").modal('hide');
                this.listadoTareas();
                this.loader(false);

                Swal.fire(
                    'Exito!',
                    'Tarea modificada satisfactoriamente',
                    'success'
                );
            })
            .catch(() => {

                $("#editar-tarea").modal('hide');
                this.loader(false);

                Swal.fire(
                    'Error!',
                    'Ocurrio un error. Por favor intenta de nuevo',
                    'error'
                );
            });
        },
        listadoProyectos(){

            axios({
                method: 'GET',
                url: '/proyectos/list/',
                headers: {
                    Authorization: getToken()
                }
            })
            .then(response => {

                if(response.data.code == 200 && response.data.status == 'success'){

                    this.proyectos = response.data.proyectos;
                }
            });
        },
        listadoInstrumentos(){

            axios({
                method: 'GET',
                url: '/instrumentos/list/',
                headers: {
                    Authorization: getToken()
                }
            })
            .then(response => {

              this.instrumentos = response.data;
            });
        },
        loader(status){

            this.loading = status;
        }
    },
    filters: {
        tipoTarea(value){

            if(value == 1){

                return "Encuesta";

            } else if(value == 2){

                return "Cartografia";
            }
        }
    }
})