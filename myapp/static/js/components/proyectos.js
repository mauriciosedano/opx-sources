proyecto = new Vue({
     el: '#gestion-proyectos',
    delimiters: ['[[', ']]'],
    created: function(){

        if(window.location.pathname == '/proyectos/'){

            this.listadoProyectos();
            this.listadoDecisiones();
            this.listadoContextos();
        }
    },
    data: {
        almacenamientoProyecto: {},
        decisiones: [],
        edicionProyecto: {},
        proyectos: [],
        contextos: []
    },
    methods: {
        listadoProyectos(){

            axios({
                method: 'GET',
                url: '/proyectos/list/',
                headers: {
                    Authorization: getToken()
                }
            })
            .then(response => {

                this.proyectos = response.data;
            });
        },
        almacenarProyecto(){

            var queryString = Object.keys(this.almacenamientoProyecto).map(key => {

                if(key == 'decisiones'){

                    let decisiones = [];

                    for(let i = 0; i < this.almacenamientoProyecto.decisiones.length; i++){

                        decisiones.push(this.almacenamientoProyecto.decisiones[i].desiid);
                    }
                    valor = JSON.stringify(decisiones);

                } else if(key == 'contextos'){

                    let contextos = [];

                    for(let i = 0; i < this.almacenamientoProyecto.contextos.length; i++){


                        contextos.push(this.almacenamientoProyecto.contextos[i].contextoid);
                    }

                    valor = JSON.stringify(contextos);

                } else{

                    valor = this.almacenamientoProyecto[key]
                }

                return key + '=' + valor
            }).join('&');

            axios({
                method: 'post',
                url: '/proyectos/store/',
                data: queryString,
                headers: {
                    'Content-type': 'application/x-www-form-urlencoded',
                    Authorization: getToken()
                }
            })
            .then(response => {

                $("#agregar-proyecto").modal('hide')
                this.almacenamientoProyecto = {};
                this.listadoProyectos();

                Swal.fire({
                  title: 'Exito!',
                  text: 'Proyecto creado satisfactoriamente',
                  type: 'success',
                  confirmButtonText: 'Acepto'
                });
            })
            .catch(response => {

                $("#agregar-proyecto").modal('hide')

                Swal.fire({
                  title: 'Error!',
                  text: 'Ocurrio un error. Por favor intenta de nuevo',
                  type: 'error',
                  confirmButtonText: 'Acepto'
                });
            });
        },
        eliminarProyecto(id){

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

                axios({
                    method: 'delete',
                    url: '/proyectos/delete/' + id,
                    headers: {
                        Authorization: getToken()
                    }
                })
                .then(response => {

                    this.listadoProyectos();

                    Swal.fire(
                      'Eliminado!',
                      'El proyecto fue eliminado de forma exitosa',
                      'success'
                    );
                })
                .catch(response => {

                     this.listadoProyectos();

                     Swal.fire(
                      'Error!',
                      'Ocurrio un error por favor intenta de nuevo',
                      'error'
                    );
                });
              }
            });
        },
        editarProyecto(){

            var queryString = Object.keys(this.edicionProyecto).map(key => {
                return key + '=' + this.edicionProyecto[key]
            }).join('&');

            axios({
                method: 'post',
                url: '/proyectos/' + this.edicionProyecto.proyid,
                data: queryString,
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    Authorization: getToken()
                }
            })
            .then(response => {

                    $("#editar-proyecto").modal('hide');
                    Swal.fire(
                        'Exito!',
                        'Proyecto modificado satisfactoriamente',
                        'success'
                    );
                    this.listadoProyectos();
            })
            .catch(() => {

                $("#editar-proyecto").modal('hide');

                Swal.fire(
                    'Error!',
                    'Ocurrio un error. Por favor intenta de nuevo',
                    'error'
                );
            })
        },
        listadoDecisiones(){

            axios({
                method: 'GET',
                url: '/decisiones/list/',
                headers: {
                    Authorization: getToken()
                }
            })
            .then(response => {

                /*for(let i = 0; i < response.data.length; i++){

                    this.decisiones.push({'track-by': response.data[i].desiid, 'label': response.data[i].desidescripcion});
                }*/
                this.decisiones = response.data;

            })
        },
        listadoContextos(){

            axios({
                method: 'GET',
                url: '/contextos/list/',
                headers: {
                    Authorization: getToken()
                }
            })
            .then(response => {

                this.contextos = response.data;
            });
        }
    }
})