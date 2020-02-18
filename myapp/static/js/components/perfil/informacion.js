let informacionPerfil = new Vue({
    el: "#informacion-perfil",
    delimiters: ['[[', ']]'],
    mounted(){

        this.getData();
    },
    data: {
        iniciales: '',
        infoUsuario: {}
    },
    methods: {
        getData(){

            let userInfo = JSON.parse(sessionStorage.getItem('userinfo'));

            if(userInfo != null && typeof userInfo == 'object' && userInfo.hasOwnProperty('user')){

                this.infoUsuario = userInfo.user;

                if(this.infoUsuario.hasOwnProperty('userfullname') && this.infoUsuario.userfullname != null){

                    this.getIniciales(this.infoUsuario.userfullname);
                }
            }
        },
        getIniciales(nombre){

            let inicialesArray = nombre.split(' ');
            inicialesArray.map((letter) => {

                this.iniciales += letter.charAt(0);
            });

        }
    }
})