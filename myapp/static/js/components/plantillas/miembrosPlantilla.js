miembrosPlantilla = new Vue({
    el: '#gestion-miembros-plantilla',
    delimiters: ['[[', ']]'],
    data: {
        plantillaID: '',
        miembrosPlantilla: [],
        usuariosDisponibles: []
    },
    created(){

        window.setTimeout(() => {
            if(window.location.pathname.substr(1, 7) == "equipos" && window.location.pathname.substr(46, 8) == "miembros"){
            
                this.listadoMiembros();
                this.listadoUsuariosDisponibles();
            }

        }, 1000);
    },
    methods: {
        listadoMiembros(){

            axios({
                url: '/miembros-plantilla/' + this.plantillaID + '/list/',
                method: 'GET',
                headers: {
                    Authorization: getToken()
                }
            })
            .then(response => {

                if(response.data.code == 200 && response.data.status == 'success'){

                    this.miembrosPlantilla = response.data.data;
                }
            });
        },
        listadoUsuariosDisponibles(){

            axios({
                url: '/miembros-plantilla/' + this.plantillaID + '/usuarios-disponibles/',
                method: 'GET',
                headers: {
                    Authorization: getToken()
                }
            })
            .then(response => {

                if(response.data.code == 200 && response.data.status == 'success'){

                    this.usuariosDisponibles = response.data.data;
                }
            });
        },
        agregarIntegrante(userid){

            axios({
                url: '/miembros-plantilla/' + this.plantillaID + '/store/',
                method: 'POST',
                data: 'userid=' + userid,
                headers: {
                    Authorization: getToken(),
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            })
            .then(response => {

                if(response.data.code == 201 && response.data.status == 'success'){

                    this.listadoMiembros();
                    this.listadoUsuariosDisponibles();
                }
            });
        },
        eliminarIntegrante(miplid){

            Swal.fire({
                text: 'Estas seguro?',
                showCancelButton: true
            })
            .then(result => {

                if(result.value){

                     axios({
                        url: '/miembros-plantilla/' + miplid + '/delete/',
                        method: 'DELETE',
                        headers: {
                            Authorization: getToken()
                        }
                    })
                    .then(response => {

                        if(response.data.code == 200 && response.data.status == 'success'){

                            this.listadoMiembros();
                            this.listadoUsuariosDisponibles();

                            Swal.fire(
                                'Exito',
                                'Miembro Eliminado correctamente del equipo',
                                'success'
                            )
                        }
                    })
                }
            });
        }
    }
})