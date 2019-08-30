let decision = new Vue({
    delimiters: ['[[', ']]'],
    el: '#gestion-decisiones',
    created(){

        this.listadoDecisiones();
        this.listadoUsuarios();
    },
    data: {
        decisiones: [],
        edicionDecision: {},
        almacenamientoDecision: {},
        usuarios: []
    },
    methods: {
        listadoDecisiones(){

            axios.get('/decisiones/list/').then(response => {

                this.decisiones = response.data;
            });
        },
        almacenarDecision(){

            var queryString = Object.keys(this.almacenamientoDecision).map(key => {
                return key + '=' + this.almacenamientoDecision[key]
            }).join('&');

            axios({
                method: 'post',
                url: '/decisiones/store/',
                data: queryString,
                headers: {
                    'Content-type': 'application/x-www-form-urlencoded'
                }
            })
            .then(response => {

                $("#agregar-decision").modal('hide')
                this.almacenamientoDecision = {};
                this.listadoDecisiones();

                Swal.fire({
                  title: 'Exito!',
                  text: 'Decisión creada satisfactoriamente',
                  type: 'success',
                  confirmButtonText: 'Acepto'
                });
            })
            .catch(response => {

                $("#agregar-decision").modal('hide')
                this.almacenamientoDecision = {};

                Swal.fire({
                  title: 'Error!',
                  text: 'Ocurrio un error. Por favor intenta de nuevo',
                  type: 'error',
                  confirmButtonText: 'Acepto'
                });
            });
        },
        eliminarDecision(id){

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

                axios.delete('/decisiones/delete/' + id)
                .then(response => {

                    this.listadoDecisiones();

                    Swal.fire(
                      'Eliminado!',
                      'La decision fue eliminada de forma exitosa',
                      'success'
                    );
                })
                .catch(response => {

                     this.listadoDecisiones();

                     Swal.fire(
                      'Error!',
                      'Ocurrio un error por favor intenta de nuevo',
                      'error'
                    );
                });
              }
            });
        },
        editarDecision(){

            var queryString = Object.keys(this.edicionDecision).map(key => {
                return key + '=' + this.edicionDecision[key];
            }).join('&');

            axios({
                method: 'post',
                url: '/decisiones/' + this.edicionDecision.desiid,
                data: queryString,
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            })
            .then(response => {

                    $("#editar-decision").modal('hide');
                    Swal.fire(
                        'Exito!',
                        'Decisión modificada satisfactoriamente',
                        'success'
                    );
                    this.listadoDecisiones();
            })
            .catch(() => {

                $("#editar-decision").modal('hide');

                Swal.fire(
                    'Error!',
                    'Ocurrio un error. Por favor intenta de nuevo',
                    'error'
                );
            });
        },
        listadoUsuarios(){

            axios.get('/usuarios/list/').then(response => {

                this.usuarios = response.data;
            });
        }
    }
})