gestionPerfil = new Vue({
    el: '#gestion-perfil',
    delimiters: ['[[', ']]'],
    data: {
        informacionUsuario: {},
        iniciales: ''
    },
    methods: {
        obtenerInformacion(){

            axios({
                url: '/usuarios/detail/' + getUser().userid,
                method: 'GET',
                headers: {
                    Authorization: getToken()
                }
            })
            .then(response => {

                if(response.data.code == 200 && response.data.status == 'success'){

                    this.informacionUsuario = response.data.usuario;

                    if(this.infoUsuario.hasOwnProperty('userfullname') && this.infoUsuario.userfullname != null){

                        this.getIniciales(this.infoUsuario.userfullname);
                    }
                }
            })
        },
        actualizarInformacion(){

            axios({
                headers: {
                    Authorization: getToken(),
                },
                data: informacionUsuario,
                method: 'POST',
                url: '/usuarios/' + getUser().userid
            })
            .then(response => {

                if(response.data.code == 200 && response.data.status = 'success'){

                    Swal.fire({
                        title: 'Exito',
                        text: 'Su información fue actualizada correctamente',
                        type: 'success'
                    });
                }
            })
            .catch(error => {

                Swal.fire({
                    title: 'Error',
                    text: 'Ocurrio un error. Por favor intenta de nuevo.',
                    type: 'error'
                });
            });
        },
        getIniciales(nombre){

            let inicialesArray = nombre.split(' ');
            inicialesArray.map((letter) => {

                this.iniciales += letter.charAt(0);
            });

        }
    }
})