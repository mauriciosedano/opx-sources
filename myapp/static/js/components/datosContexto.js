let datoContexto = new Vue({
    delimiters: ['[[', ']]'],
    el: '#gestion-datos-contexto',
    created(){

        if(window.location.pathname.substr(1, 15) == "contextos/datos"){

            this.contextoID = window.location.pathname.substr(17, 41);
            this.listadoDatosContexto();
        }
    },
    data: {
        contextoID: 0,
        datosContexto: [],
        edicionDatoContexto: {},
        almacenamientoDatoContexto: {}
    },
    methods: {
        listadoDatosContexto(){

            axios({
                method: 'GET',
                url: '/datos-contexto/list/' + this.contextoID,
                headers: {
                    Authorization: getToken()
                }
            })
            .then(response => {

                this.datosContexto = response.data.datosContexto;
            });
        },
        almacenarDatoContexto(){

            formData = new FormData(document.getElementById('registro-dato-contexto'))
            formData.append('contextoid', this.contextoID);

            axios({
                method: 'post',
                url: '/datos-contexto/store/',
                data: formData,
                headers: {
                    'Content-type': 'application/x-www-form-urlencoded',
                    Authorization: getToken()
                }
            })
            .then(response => {

                $("#agregar-dato-contexto").modal('hide');
                this.almacenamientoDatoContexto = {};
                this.listadoDatosContexto();

                Swal.fire({
                  title: 'Exito!',
                  text: 'Dato de Contexto creado satisfactoriamente',
                  type: 'success',
                  confirmButtonText: 'Acepto'
                });
            })
            .catch(error => {

                if(error.response.status == 400){

                    Swal.fire({
                      title: 'Error!',
                      text: 'El archivo no fue enviado no es de tipo CSV',
                      type: 'error',
                      confirmButtonText: 'Acepto'
                    });

                } else{

                    Swal.fire({
                      title: 'Error!',
                      text: 'Ocurrio un error. Por favor intenta de nuevo',
                      type: 'error',
                      confirmButtonText: 'Acepto'
                    });
                }
            });
        },
        eliminarDatoContexto(id){

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
                    url: '/datos-contexto/delete/' + id,
                    headers: {
                        Authorization: getToken()
                    }
                })
                .then(response => {

                    this.listadoDatosContexto();

                    Swal.fire(
                      'Eliminado!',
                      'El dato de contexto fue eliminado de forma exitosa',
                      'success'
                    );
                })
                .catch(response => {

                     this.listadoDatosContexto();

                     Swal.fire(
                      'Error!',
                      'Ocurrio un error por favor intenta de nuevo',
                      'error'
                    );
                });
              }
            });
        },
        editarDatoContexto(){

            formData = new FormData(document.getElementById('edicion-dato-contexto'))
            formData.append('contextoid', this.contextoID);

            axios({
                method: 'post',
                url: '/datos-contexto/' + this.edicionDatoContexto.dataid,
                data: formData,
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    Authorization: getToken()
                }
            })
            .then(response => {

                $("#editar-dato-contexto").modal('hide');

                Swal.fire(
                    'Exito!',
                    'Dato de Contexto modificado satisfactoriamente',
                    'success'
                );

                this.listadoDatosContexto();
            })
            .catch(error => {

                //$("#editar-dato-contexto").modal('hide');

                if(error.response.status == 400){

                    Swal.fire({
                      title: 'Error!',
                      text: 'El archivo no es de tipo CSV',
                      type: 'error',
                      confirmButtonText: 'Acepto'
                    });

                } else{

                    Swal.fire(
                        'Error!',
                        'Ocurrio un error. Por favor intenta de nuevo',
                        'error'
                    );
                }
            });
        }
    }
})