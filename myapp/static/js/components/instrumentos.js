let instrumento = new Vue({
    delimiters: ['[[', ']]'],
    el: '#gestion-instrumentos',
    created(){

        if(window.location.pathname == '/instrumentos/'){

            this.listadoInstrumentos();
        }
    },
    data: {
        instrumentos: [],
        almacenamientoInstrumento: {},
        edicionInstrumento: {}
    },
    methods: {
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
        almacenarInstrumento(){

            var queryString = Object.keys(this.almacenamientoInstrumento).map(key => {
                return key + '=' + this.almacenamientoInstrumento[key]
            }).join('&');

            axios({
                method: 'post',
                url: '/instrumentos/store/',
                data: queryString,
                headers: {
                    'Content-type': 'application/x-www-form-urlencoded',
                    Authorization: getToken()
                }
            })
            .then(response => {

                $("#agregar-instrumento").modal('hide')
                this.almacenamientoInstrumento = {};
                this.listadoInstrumentos();

                Swal.fire({
                  title: 'Exito!',
                  text: 'Instrumento creado satisfactoriamente',
                  type: 'success',
                  confirmButtonText: 'Acepto'
                });
            })
            .catch(response => {

                $("#agregar-instrumento").modal('hide')
                this.almacenamientoInstrumento = {};

                Swal.fire({
                  title: 'Error!',
                  text: 'Ocurrio un error. Por favor intenta de nuevo',
                  type: 'error',
                  confirmButtonText: 'Acepto'
                });
            });
        },
        eliminarInstrumento(id){

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
                    url: '/instrumentos/delete/' + id,
                    headers: {
                        Authorization: getToken()
                    }
                })
                .then(response => {

                    this.listadoInstrumentos();

                    Swal.fire(
                      'Eliminado!',
                      'El instrumento fue eliminado de forma exitosa',
                      'success'
                    );
                })
                .catch(response => {

                     this.listadoInstrumentos();

                     Swal.fire(
                      'Error!',
                      'Ocurrio un error por favor intenta de nuevo',
                      'error'
                    );
                });
              }
            });
        },
        editarInstrumento(){

            var queryString = Object.keys(this.edicionInstrumento).map(key => {

                return key + '=' + this.edicionInstrumento[key];

            }).join('&');

            axios({
                method: 'post',
                url: '/instrumentos/' + this.edicionInstrumento.instrid,
                data: queryString,
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    Authorization: getToken()
                }
            })
            .then(response => {

                    $("#editar-instrumento").modal('hide');
                    Swal.fire(
                        'Exito!',
                        'Instrumento modificado satisfactoriamente',
                        'success'
                    );
                    this.listadoInstrumentos();
            })
            .catch(() => {

                $("#editar-instrumento").modal('hide');

                Swal.fire(
                    'Error!',
                    'Ocurrio un error. Por favor intenta de nuevo',
                    'error'
                );
            });
        },
        verificarImplementacionEncuesta(id){

            return new Promise((resolve, reject) => {

                axios({
                    method: 'GET',
                    url: '/instrumentos/' + id + '/verificar-implementacion/',
                    headers: {
                        Authorization: getToken()
                    }
                })
                .then(response => {

                    if(response.data.code == 200){

                        resolve(response.data.implementacion);
                    }
                })
                .catch(response => {

                    reject(false);
                });

            });
        },
        async implementarEncuesta(id){

            await this.verificarImplementacionEncuesta(id)
            .then(response => {

                if(!response){

                    axios({
                        method: 'GET',
                        url: '/instrumentos/' + id + '/implementar/',
                        headers: {
                            Authorization: getToken()
                        }
                    })
                    .then(response => {

                        Swal.fire({
                            title: 'Exito',
                            text: 'La encuesta fue implementada exitosamente',
                            type: 'success'
                        });

                    })
                    .catch( error => {

                        Swal.fire({
                            title: 'Error',
                            text: 'Ocurrio un error. Por favor intenta de nuevo',
                            type: 'error'
                        });
                    });

                } else{

                    Swal.fire({
                        title: 'Implementado',
                        text: 'El instrumento ya se encuentra implementado',
                        type: 'warning'
                    });
                }
            })
            .catch( error => {

                Swal.fire({
                    title: 'Error',
                    text: 'Ocurrio un error. Por favor intenta de nuevo',
                    type: 'error'
                });
            })
        },
        async informacionEncuesta(id){

            await this.verificarImplementacionEncuesta(id)
            .then(response => {

                if(response){

                    location.href = '/instrumentos/informacion/' + id;

                } else{

                    Swal.fire({
                        title: 'Error',
                        text: 'El formulario no se encuentra implementado',
                        type: 'error'
                    });
                }
            })
            .catch(error => {

                Swal.fire({
                    title: 'Error',
                    text: 'Ocurrio un error. Por favor intenta de nuevo',
                    type: 'warning'
                });
            });
        }
    },
    filters: {
        tipoInstrumento(value){

            if(value == 1){

                return "Encuesta";

            } else if(value == 2){

                return "Cartografía";
            }
        }
    }
});