let rol = new Vue({
    delimiters: ['[[', ']]'],
    el: '#gestion-permisos-rol',
    created(){

        this.listadoPermisos();

    },
    data: {
        rolID: 0,
        permisos: [],
        //edicionRol: {},
        almacenamientoPermiso: {},
    },
    methods: {
        listadoPermisos(){

            this.rolID = window.location.pathname.substr(16, 36);

            axios.get('/funciones-rol/list/' + this.rolID).then(response => {

                this.permisos = response.data;
            });
        },
        almacenarPermiso(){

            this.almacenamientoPermiso.rolid = this.rolID;

            var queryString = Object.keys(this.almacenamientoPermiso).map(key => {
                return key + '=' + this.almacenamientoPermiso[key]
            }).join('&');

            axios({
                method: 'post',
                url: '/funciones-rol/store/',
                data: queryString,
                headers: {
                    'Content-type': 'application/x-www-form-urlencoded'
                }
            })
            .then(response => {

                $("#agregar-permiso").modal('hide')
                this.almacenamientoPermiso = {};
                this.listadoPermisos();

                Swal.fire({
                  title: 'Exito!',
                  text: 'Permiso asignado satisfactoriamente',
                  type: 'success',
                  confirmButtonText: 'Acepto'
                });
            })
            .catch(response => {

                $("#agregar-permiso").modal('hide')
                this.almacenamientoPermiso = {};

                Swal.fire({
                  title: 'Error!',
                  text: 'Ocurrio un error. Por favor intenta de nuevo',
                  type: 'error',
                  confirmButtonText: 'Acepto'
                });
            });
        },
        eliminarPermiso(id){

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

                axios.delete('/funciones-rol/delete/' + id)
                .then(response => {

                    this.listadoPermisos();

                    Swal.fire(
                      'Eliminado!',
                      'El permiso fue eliminado de forma exitosa',
                      'success'
                    );
                })
                .catch(response => {

                     this.listadoPermisos();

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