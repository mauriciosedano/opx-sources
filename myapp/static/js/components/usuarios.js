let usuario = new Vue({
    delimiters: ['[[', ']]'],
    el: '#gestion-usuarios',
    created(){

        if(window.location.pathname == '/usuarios/'){

            this.listadoUsuarios();
            this.listadoRoles();
        }
    },
    data: {
        usuarios: [],
        edicionUsuario: {},
        almacenamientoUsuario: {},
        roles: []
    },
    methods: {
        listadoUsuarios(){

            axios({
                method: 'GET',
                url: '/usuarios/list/',
                headers: {
                    Authorization: getToken()
                }
            })
            .then(response => {

                this.usuarios = response.data;
            });
        },
        almacenarUsuario(){

            var queryString = Object.keys(this.almacenamientoUsuario).map(key => {
                return key + '=' + this.almacenamientoUsuario[key]
            }).join('&');

            axios({
                method: 'post',
                url: '/usuarios/store/',
                data: queryString,
                headers: {
                    'Content-type': 'application/x-www-form-urlencoded',
                    Authorization: getToken()
                }
            })
            .then(response => {

                $("#agregar-usuario").modal('hide')
                this.almacenamientoUsuario = {};
                this.listadoUsuarios();

                Swal.fire({
                  title: 'Exito!',
                  text: 'Usuario creado satisfactoriamente',
                  type: 'success',
                  confirmButtonText: 'Acepto'
                });
            })
            .catch(response => {

                $("#agregar-usuario").modal('hide')
                this.almacenamientoUsuario = {};

                Swal.fire({
                  title: 'Error!',
                  text: 'Ocurrio un error. Por favor intenta de nuevo',
                  type: 'error',
                  confirmButtonText: 'Acepto'
                });
            });
        },
        eliminarUsuario(id){

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
                    method: "DELETE",
                    url: '/usuarios/delete/' + id,
                    headers: {
                        Authorization: getToken()
                    }
                })
                .then(response => {

                    this.listadoUsuarios();

                    Swal.fire(
                      'Eliminado!',
                      'El usuario fue eliminado de forma exitosa',
                      'success'
                    );
                })
                .catch(response => {

                             this.listadoUsuarios();

                     Swal.fire(
                      'Error!',
                      'Ocurrio un error por favor intenta de nuevo',
                      'error'
                    );
                });
              }
            });
        },
        editarUsuario(){

            var queryString = Object.keys(this.edicionUsuario).map(key => {
                return key + '=' + this.edicionUsuario[key];
            }).join('&');

            axios({
                method: 'post',
                url: '/usuarios/' + this.edicionUsuario.userid,
                data: queryString,
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    Authorization: getToken()
                }
            })
            .then(response => {

                    $("#editar-usuario").modal('hide');

                    this.listadoUsuarios();

                    Swal.fire(
                        'Exito!',
                        'Usuario modificado satisfactoriamente',
                        'success'
                    );
            })
            .catch(() => {

                $("#editar-usuario").modal('hide');

                Swal.fire(
                    'Error!',
                    'Ocurrio un error. Por favor intenta de nuevo',
                    'error'
                );
            });
        },
        listadoRoles(){

            axios({
                method: 'GET',
                url: '/roles/list/',
                headers: {
                    Authorization: getToken()
                }
            }).then(response => {

                this.roles = response.data;
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
});