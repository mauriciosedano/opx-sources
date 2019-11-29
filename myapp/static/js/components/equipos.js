let equipo = new Vue({
    delimiters: ['[[', ']]'],
    el: '#gestion-equipo',
    data: {
        equipo: [],
        usuariosDisponibles: [],
        proyectoID: '',
        loading: false,
    },
    created(){

        if(window.location.pathname.substr(1, 16) == "equipos/proyecto"){

            this.proyectoID = window.location.pathname.substr(18);
            this.obtenerEquipo();
            this.obtenerUsuariosDisponibles();
        }
    },
    methods: {
        obtenerEquipo(){

            this.loader(true);

            axios({
                url: '/equipos/list/' + this.proyectoID,
                method: 'GET',
                headers: {
                    Authorization: getToken()
                }
            })
            .then(response => {

                this.loader(false);

                if(response.data.code == 200 && response.data.status == 'success'){

                    this.equipo = response.data.equipo;
                }
            });
        },
        obtenerUsuariosDisponibles(){

            axios({
                url: '/equipos/' + this.proyectoID + "/usuarios-disponibles/",
                method: 'GET',
                headers: {
                    Authorization: getToken()
                }
            })
            .then(response => {

                if(response.data.code == 200 && response.data.status == 'success'){

                    this.usuariosDisponibles = response.data.usuarios;
                }
            })
        },
        addIntegrante(userID){

            data = "userid=" + userID + "&proyid=" + this.proyectoID;

            axios({
                url: '/equipos/store/',
                method: 'POST',
                data: data,
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    Authorization: getToken()
                }
            })
            .then(response => {

                if(response.data.code == 201 && response.data.status == 'success'){

                    this.obtenerEquipo();
                    this.obtenerUsuariosDisponibles();
                }
            });
        },
        eliminarIntegrante(equID){

            axios({
                url: '/equipos/delete/' + equID,
                method: 'DELETE',
                headers: {
                    Authorization: getToken()
                }
            })
            .then(response => {

                if(response.data.code == 200 && response.data.status == 'success'){

                    this.obtenerEquipo();
                    this.obtenerUsuariosDisponibles();
                }
            })
        },
        loader(status){

            this.loading = status;
        }
    }
})