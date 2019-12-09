estadisticas = new Vue({
    el: '#dashboard',
    delimiters: ['[[', ']]'],
    created(){

        if(window.location.pathname == '/dashboard/'){

           this.obtenerCantidadUsuarios();
           this.usuariosXRol();
           this.obtenerRanking();
           this.listadoProyectos();
        }
    },
    data: {

        cantidadUsuarios: 0,
        ranking: []
    },
    methods: {
        obtenerCantidadUsuarios(){

            axios({
                url: '/estadisticas/cantidad-usuarios/',
                method: 'GET',
                headers: {
                    Authorization: getToken()
                }
            })
            .then(response => {

                this.cantidadUsuarios = response.data.data;
            })
        },
        usuariosXRol(){

            axios({
                url: '/estadisticas/usuarios-x-rol/',
                method: 'GET',
                headers: {
                    Authorization: getToken()
                }
            })
            .then(response => {

                let data = response.data.data;

                let ctx = document.getElementById("usuarios-rol").getContext('2d')
                new Chart(ctx, {
                    type: 'bar',
                    data: {
                      labels: data.roles,
                      datasets: [
                        {
                          label: "Usuarios x Rol",
                          backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
                          data: data.cantidadUsuarios
                        }
                      ]
                    },
                    options: {
                      title: {
                        display: true,
                        text: 'Usuarios x Rol'
                      }
                    }
                });
            })


        },
        obtenerRanking(){

            axios({
                url: '/estadisticas/ranking/',
                method: 'GET',
                headers: {
                    Authorization: getToken()
                }
            })
            .then(response => {

                this.ranking = response.data.data;
            })
        },
        listadoProyectos(){

            axios({
                url: '/estadisticas/proyectos-tareas/',
                method: 'GET',
                headers: {
                    Authorization: getToken()
                }
            })
            .then(response => {

                if(response.data.code == 200 && response.data.status == 'success'){

                    new Gantt('#proyectos-gantt', response.data.data, {
                        on_click: (task) => {

                            if(task.type == 'project'){

                                statsPromises = [this.tareasXTipo(task.id), this.tareasXEstado(task.id)];

                                Promise.all(statsPromises)
                                .then(() => {

                                    console.log("bn");
                                    $("#estadisticas-tareas").modal('show');
                                })
                                .catch((reason) => {
                                    console.log(reason)
                                    Swal.fire({
                                        title: 'Error',
                                        text: 'Ocurrio un error. Por favor intenta de nuevo',
                                        type: 'error'
                                    });
                                });
                            }
                        }
                    });
                }
            });
        },
        tareasXTipo(proyectoID){

            return new Promise((resolve,reject) => {

                axios({
                    url: '/estadisticas/' + proyectoID + '/tareas-x-tipo/',
                    method: 'GET',
                    headers: {
                        Authorization: getToken()
                    }
                })
                .then(response => {

                    if(response.data.code == 200 && response.data.status == 'success'){

                        let data = response.data.data;

                        let ctx = document.getElementById("tareas-x-tipo").getContext('2d')
                        new Chart(ctx, {
                            type: 'doughnut',
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

                        resolve("");

                    } else{

                        reject("");
                    }
                })
            })
        },
        tareasXEstado(proyectoID){

            return new Promise((resolve,reject) => {

                axios({
                    url: '/estadisticas/' + proyectoID + '/tareas-x-estado/',
                    method: 'GET',
                    headers: {
                        Authorization: getToken()
                    }
                })
                .then(response => {

                    if(response.data.code == 200 && response.data.status == 'success'){

                        let data = response.data.data;

                        let ctx = document.getElementById("tareas-x-estado").getContext('2d')
                        new Chart(ctx, {
                            type: 'doughnut',
                            data: {
                              labels: data.estados,
                              datasets: [
                                {
                                  label: "Tareas Por Estado",
                                  backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
                                  data: data.cantidad
                                }
                              ]
                            },
                            options: {
                              title: {
                                display: true,
                                text: 'Tareas Por Estado'
                              }
                            }
                        });

                        resolve("");

                    } else{

                        reject("");
                    }
                })
            });
        }
    }
})