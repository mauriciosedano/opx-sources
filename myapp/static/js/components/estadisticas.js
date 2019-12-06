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
                    type: 'doughnut',
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
                url: '/proyectos/list/',
                method: 'GET',
                params: {
                    all: 1
                },
                headers: {
                    Authorization: getToken()
                }
            })
            .then(response => {

                anychart.onDocumentReady(function () {
	            // create data

	            proyectos = response.data.proyectos;
	            data = []

	            for(let i= 0; i<proyectos.length; i++){

	                let id = i+1
	                id = id.toString(10)

	                fechaInicio = proyectos[i].proyfechainicio.split("-")
	                fechaFin = proyectos[i].proyfechacierre.split("-")

	                anioA = parseInt(fechaInicio[0], 10)
	                mesA = parseInt(fechaInicio[1], 10)
	                diaA = parseInt(fechaInicio[2], 10)

	                anioB = parseInt(fechaFin[0], 10)
	                mesB = parseInt(fechaFin[1], 10)
	                diaB = parseInt(fechaFin[2], 10)

	                data.push({
	                    id: id,
	                    name: proyectos[i].proynombre,
	                    actualStart: Date(anioA, mesA, diaA),
                        actualEnd: Date(anioB, mesB, diaB)
	                });
	            }

	            console.log(data)/

                console.log(data);
                // create a data tree
                var treeData = anychart.data.tree(data, "as-tree");

                // create a chart
                var chart = anychart.ganttProject();

                // set the data
                chart.data(treeData);
                // configure the scale
                chart.getTimeline().scale().maximum(Date.UTC(2019, 12, 31));
                // set the container id
                chart.container("gantt");
                // initiate drawing the chart
                chart.draw();
                // fit elements to the width of the timeline
                chart.fitAll();
            });
            });
        }
    }
})