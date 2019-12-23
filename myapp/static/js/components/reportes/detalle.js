estadisticas = new Vue({
    el: '#reportes-detalle-proyecto',
    delimiters: ['[[', ']]'],
    data: {
        proyectoID: ''
    },
    created(){

        if(window.location.pathname.substr(1, 8) == "reportes" && window.location.pathname.substr(47, 7) == "detalle"){

            window.setTimeout(() => {

                this.tiposTarea();
                this.usuariosXBarrio();
                this.usuariosXNivelEducativo();
                this.usuariosXRol();
                this.usuariosXGenero();
            }, 1000);
        }
    },
    methods:{
        tiposTarea(){
            axios({
                url: '/estadisticas/' + this.proyectoID + '/tareas-x-tipo/',
                method: 'GET',
                headers: {
                    Authorization: getToken()
                }
            })
            .then(response => {

                if(response.data.code == 200 && response.data.status == 'success'){

                    let ctx = document.getElementById('tipos-tarea').getContext('2d');
                    let data = response.data.data;

                    new Chart(ctx, {
                        type: 'pie',
                        data: {
                          labels: data.tipos,
                          datasets: [
                            {
                              label: "Tareas Por Tipo",
                              backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
                              data: data.cantidad
                            }
                          ]
                        },
                        options: {
                          title: {
                            display: true,
                            text: 'Tareas Por Tipo'
                          }
                        }
                    });
                }
            })
        },
        usuariosXBarrio(){
            axios({
                url: '/estadisticas/' + this.proyectoID + '/usuarios-x-barrio/',
                method: 'GET',
                headers: {
                    Authorization: getToken()
                }
            })
            .then(response => {

                if(response.data.code == 200 && response.data.status == 'success'){

                    let ctx = document.getElementById('usuarios-barrio').getContext('2d');
                    let data = response.data.data;

                    new Chart(ctx, {
                        type: 'pie',
                        data: {
                          labels: data.barrios,
                          datasets: [
                            {
                              label: "Usuarios Por Barrio",
                              backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
                              data: data.cantidad
                            }
                          ]
                        },
                        options: {
                          title: {
                            display: true,
                            text: 'Usuarios Por Barrio'
                          }
                        }
                    });
                }
            })
        },
        usuariosXNivelEducativo(){
            axios({
                url: '/estadisticas/' + this.proyectoID + '/usuarios-x-nivel-educativo/',
                method: 'GET',
                headers: {
                    Authorization: getToken()
                }
            })
            .then(response => {

                if(response.data.code == 200 && response.data.status == 'success'){

                    let ctx = document.getElementById('usuarios-nivel-educativo').getContext('2d');
                    let data = response.data.data;

                    new Chart(ctx, {
                        type: 'pie',
                        data: {
                          labels: data.niveles_educativos,
                          datasets: [
                            {
                              label: "Usuarios Por Nivel Educativo",
                              backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
                              data: data.cantidad
                            }
                          ]
                        },
                        options: {
                          title: {
                            display: true,
                            text: 'Usuarios Por Nivel Educativo'
                          }
                        }
                    });
                }
            })
        },
        usuariosXRol(){
            axios({
                url: '/estadisticas/' + this.proyectoID + '/usuarios-x-rol/',
                method: 'GET',
                headers: {
                    Authorization: getToken()
                }
            })
            .then(response => {

                if(response.data.code == 200 && response.data.status == 'success'){

                    let ctx = document.getElementById('usuarios-rol').getContext('2d');
                    let data = response.data.data;

                    new Chart(ctx, {
                        type: 'pie',
                        data: {
                          labels: data.roles,
                          datasets: [
                            {
                              label: "Usuarios Por Rol",
                              backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
                              data: data.cantidad
                            }
                          ]
                        },
                        options: {
                          title: {
                            display: true,
                            text: 'Usuarios Por Rol'
                          }
                        }
                    });
                }
            })
        },
        usuariosXGenero(){
            axios({
                url: '/estadisticas/' + this.proyectoID + '/usuarios-x-genero/',
                method: 'GET',
                headers: {
                    Authorization: getToken()
                }
            })
            .then(response => {

                if(response.data.code == 200 && response.data.status == 'success'){

                    let ctx = document.getElementById('usuarios-genero').getContext('2d');
                    let data = response.data.data;

                    new Chart(ctx, {
                        type: 'pie',
                        data: {
                          labels: data.generos,
                          datasets: [
                            {
                              label: "Usuarios Por Género",
                              backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
                              data: data.cantidad
                            }
                          ]
                        },
                        options: {
                          title: {
                            display: true,
                            text: 'Usuarios Por Género'
                          }
                        }
                    });
                }
            })
        }
    }
})