let contexto = new Vue({
    delimiters: ['[[', ']]'],
    el: '#gestion-contextos',
    created(){
        if(window.location.pathname == '/contextos/'){

            this.listadoContextos();
        }
    },
    data: {
        contextos: [],
        edicionContexto: {},
        almacenamientoContexto: {}
    },
    methods: {
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
        },
        almacenarContexto(){

            var queryString = Object.keys(this.almacenamientoContexto).map(key => {
                return key + '=' + this.almacenamientoContexto[key]
            }).join('&');

            axios({
                method: 'post',
                url: '/contextos/store/',
                data: queryString,
                headers: {
                    'Content-type': 'application/x-www-form-urlencoded',
                    Authorization: getToken()
                }
            })
            .then(response => {

                $("#agregar-contexto").modal('hide');
                this.almacenamientoContexto = {};
                this.listadoContextos();

                Swal.fire({
                  title: 'Exito!',
                  text: 'Contexto creado satisfactoriamente',
                  type: 'success',
                  confirmButtonText: 'Acepto'
                });
            })
            .catch(response => {

                $("#agregar-contexto").modal('hide')
                this.almacenamientoContexto = {};

                Swal.fire({
                  title: 'Error!',
                  text: 'Ocurrio un error. Por favor intenta de nuevo',
                  type: 'error',
                  confirmButtonText: 'Acepto'
                });
            });
        },
        eliminarContexto(id){

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
                    method: 'DELETE',
                    url: '/contextos/delete/' + id,
                    headers: {
                        Authorization: getToken()
                    }
                })
                .then(response => {

                    this.listadoContextos();

                    Swal.fire(
                      'Eliminado!',
                      'El contexto fue eliminado de forma exitosa',
                      'success'
                    );
                })
                .catch(response => {

                     this.listadoContextos();

                     Swal.fire(
                      'Error!',
                      'Ocurrio un error por favor intenta de nuevo',
                      'error'
                    );
                });
              }
            });
        },
        editarContexto(){

            var queryString = Object.keys(this.edicionContexto).map(key => {
                return key + '=' + this.edicionContexto[key];
            }).join('&');

            axios({
                method: 'post',
                url: '/contextos/' + this.edicionContexto.contextoid,
                data: queryString,
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    Authorization: getToken()
                }
            })
            .then(response => {

                    $("#editar-contexto").modal('hide');

                    Swal.fire(
                        'Exito!',
                        'Contexto modificado satisfactoriamente',
                        'success'
                    );

                    this.listadoContextos();
            })
            .catch(() => {

                $("#editar-contexto").modal('hide');

                Swal.fire(
                    'Error!',
                    'Ocurrio un error. Por favor intenta de nuevo',
                    'error'
                );
            });
        }
    }
})