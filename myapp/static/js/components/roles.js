let rol = new Vue({
    delimiters: ['[[', ']]'],
    el: '#gestion-roles',
    created(){

        this.listadoRoles();

    },
    data: {
        roles: [],
        edicionRol: {},
        almacenamientoRol: {},
    },
    methods: {
        listadoRoles(){

            axios.get('/roles/list/').then(response => {

                this.roles = response.data;
            });
        },
        almacenarRol(){

            var queryString = Object.keys(this.almacenamientoRol).map(key => {
                return key + '=' + this.almacenamientoRol[key]
            }).join('&');

            axios({
                method: 'post',
                url: '/roles/store/',
                data: queryString,
                headers: {
                    'Content-type': 'application/x-www-form-urlencoded'
                }
            })
            .then(response => {

                $("#agregar-rol").modal('hide')
                this.almacenamientoRol = {};
                this.listadoRoles();

                Swal.fire({
                  title: 'Exito!',
                  text: 'Rol creado satisfactoriamente',
                  type: 'success',
                  confirmButtonText: 'Acepto'
                });
            })
            .catch(response => {

                $("#agregar-rol").modal('hide')
                this.almacenamientoRol = {};

                Swal.fire({
                  title: 'Error!',
                  text: 'Ocurrio un error. Por favor intenta de nuevo',
                  type: 'error',
                  confirmButtonText: 'Acepto'
                });
            });
        },
        eliminarRol(id){

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

                axios.delete('/roles/delete/' + id)
                .then(response => {

                    this.listadoRoles();

                    Swal.fire(
                      'Eliminado!',
                      'El rol fue eliminado de forma exitosa',
                      'success'
                    );
                })
                .catch(response => {

                     this.listadoRoles();

                     Swal.fire(
                      'Error!',
                      'Ocurrio un error por favor intenta de nuevo',
                      'error'
                    );
                });
              }
            });
        },
        editarRol(){

            var queryString = Object.keys(this.edicionRol).map(key => {
                return key + '=' + this.edicionRol[key];
            }).join('&');

            axios({
                method: 'post',
                url: '/roles/' + this.edicionRol.rolid,
                data: queryString,
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            })
            .then(response => {

                    $("#editar-rol").modal('hide');
                    Swal.fire(
                        'Exito!',
                        'Rol modificado satisfactoriamente',
                        'success'
                    );
                    this.listadoRoles();
            })
            .catch(() => {

                $("#editar-rol").modal('hide');

                Swal.fire(
                    'Error!',
                    'Ocurrio un error. Por favor intenta de nuevo',
                    'error'
                );
            });
        }
    }
})