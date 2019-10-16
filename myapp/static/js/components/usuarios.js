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
        roles: [],
        loading: false
    },
    methods: {
        listadoUsuarios(){

            this.loader(true);

            axios({
                method: 'GET',
                url: '/usuarios/list/',
                headers: {
                    Authorization: getToken()
                }
            })
            .then(response => {

                this.usuarios = response.data;
                this.loader(false);
            });
        },
        almacenarUsuario(){

            this.loader(true);

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

                this.loader(false);

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

                this.loader(false);

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

                this.loader(true);

                axios({
                    method: "DELETE",
                    url: '/usuarios/delete/' + id,
                    headers: {
                        Authorization: getToken()
                    }
                })
                .then(response => {

                    this.listadoUsuarios();

                    this.loader(false);

                    Swal.fire(
                      'Eliminado!',
                      'El usuario fue eliminado de forma exitosa',
                      'success'
                    );
                })
                .catch(response => {

                     this.listadoUsuarios();

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
        editarUsuario(){

            this.loader(true);

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

                    this.loader(false);

                    Swal.fire(
                        'Exito!',
                        'Usuario modificado satisfactoriamente',
                        'success'
                    );
            })
            .catch(() => {

                $("#editar-usuario").modal('hide');

                this.loader(false);

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

                if(response.data.code == 200 && response.data.status == 'success'){

                    this.roles = response.data.roles;
                }
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
});