let tarea = new Vue({
    delimiters: ['[[', ']]'],
    el: '#gestion-tareas',
    created(){

        this.listadoTareas();
        this.listadoProyectos();
        this.listadoInstrumentos();
    },
    data: {
        tareas: [],
        edicionTarea: {},
        almacenamientoTarea: {},
        proyectos: [],
        instrumentos: []
    },
    methods: {
        listadoTareas(){

            axios.get('/tareas/list/').then(response => {

                this.tareas = response.data;
            });
        },
        almacenarTarea(){

            var queryString = Object.keys(this.almacenamientoTarea).map(key => {
                return key + '=' + this.almacenamientoTarea[key]
            }).join('&');

            axios({
                method: 'post',
                url: '/tareas/store/',
                data: queryString,
                headers: {
                    'Content-type': 'application/x-www-form-urlencoded'
                }
            })
            .then(response => {

                $("#agregar-tarea").modal('hide')
                this.almacenamientoTarea = {};
                this.listadoTareas();

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

                axios.delete('/tareas/delete/' + id)
                .then(response => {

                    this.listadoTareas();

                    Swal.fire(
                      'Eliminado!',
                      'La tarea fue eliminada de forma exitosa',
                      'success'
                    );
                })
                .catch(response => {

                     this.listadoTareas();

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
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            })
            .then(response => {

                $("#editar-tarea").modal('hide');

                this.listadoTareas();

                Swal.fire(
                    'Exito!',
                    'Tarea modificada satisfactoriamente',
                    'success'
                );
            })
            .catch(() => {

                $("#editar-tarea").modal('hide');

                Swal.fire(
                    'Error!',
                    'Ocurrio un error. Por favor intenta de nuevo',
                    'error'
                );
            });
        },
        listadoProyectos(){

            axios.get('/proyectos/list/').then(response => {

                this.proyectos = response.data;
            });
        },
        listadoInstrumentos(){

            axios.get('/instrumentos/list/').then(response => {

              this.instrumentos = response.data;
            });
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