gestionProyecto = new Vue({
    el: '#gestion-proyectos-mapa',
    delimiters: ['[[', ']]'],
    data: {
        informacionProyecto: {},
        map: {},
        proyectos: [],
        proyectoGestion: {},
        tareaGestion: {}
    },
    created(){

        if(window.location.pathname == '/proyectos/gestion/'){

            this.cargarMapa();
            this.obtenerProyectos();
        }
    },
    methods: {
        cargarMapa(layer){

            window.setTimeout(() => {

                this.map = L.map('map',  {
                center: [3.450572, -76.538705],
                drawControl: false,
                zoom: 13
            });

                L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
                }).addTo(this.map);

                L.tileLayer.wms('http://ws-idesc.cali.gov.co:8081/geoserver/wms?service=WMS', {
                  layers: 'idesc:mc_barrios',
                  format: 'image/png',
                  transparent: !0,
                  version: '1.1.0'
                }).addTo(this.map);

                if(layer){

                    L.geoJSON(layer,
                    {
                        onEachFeature: function(feature, layer){
                            console.log(feature)
                            console.log(layer)

                            layer.on('click', () => {

                                if(feature.properties.type == 'dimension'){

                                    axios({
                                        url: '/proyectos/detail/' + feature.properties.id,
                                        headers: {
                                            Authorization: getToken()
                                        }
                                    })
                                    .then(response => {

                                        if(response.data.code == 200 && response.data.status == 'success'){
                                            console.log('entro')
                                            this.proyectoGestion = response.data.detail.proyecto;
                                            $("#gestion-proyecto").modal('show');
                                        }
                                    })
                                    .catch(() => {

                                        Swal.fire({
                                            title: 'Error',
                                            text: 'No se puedo recuperar la información del Proyecto',
                                            type: 'error'
                                        });
                                    });

                                } else if(feature.properties.type == 'tarea'){

                                    axios({
                                        url: '/tareas/detail/' + feature.properties.id,
                                        headers: {
                                            Authorization: getToken()
                                        }
                                    })
                                    .then(response => {

                                        if(response.data.code == 200 && response.data.status == 'success'){
                                            console.log('entro')
                                            this.tareaGestion = response.data.tarea;
                                            $("#gestion-objetivo-tarea").modal('show');
                                        }
                                    })
                                    .catch(() => {

                                        Swal.fire({
                                            title: 'Error',
                                            text: 'No se puedo recuperar la información de la Tarea',
                                            type: 'error'
                                        });
                                    });
                                }
                            })
                        }
                    })
                    .addTo(this.map)
                }
            }, 1000);

        },
        eliminarMapa(){

            this.map.remove();
        },
        obtenerProyectos(){

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

                if(response.data.code == 200 && response.data.status == 'success'){

                    this.proyectos = response.data.proyectos;
                }
            })
        },
        cargarInformacionProyecto(informacionProyecto){

            this.eliminarMapa();

            if(informacionProyecto.hasOwnProperty('dimensiones_territoriales')){

                dimensiones = informacionProyecto.dimensiones_territoriales;
                cantidadDimensiones = informacionProyecto.dimensiones_territoriales.length;

                if(cantidadDimensiones > 0){

                    features = []

                    for(let i=0; i<cantidadDimensiones; i++){

                        // Añadiendo Dimensiones geográficas
                        let feature = JSON.parse(dimensiones[i].geojson)
                        feature.properties = {
                            type: 'dimension',
                            id: dimensiones[i].proyid
                        }

                        features.push(feature)

                        tareas = dimensiones[i].tareas;
                        cantidadTareas = dimensiones[i].tareas.length;

                        if(cantidadTareas > 0){

                            for(let j=0; j<cantidadTareas; j++){

                                let feature = JSON.parse(tareas[j].geojson_subconjunto)
                                feature.properties = {
                                    type: 'tarea',
                                    id: tareas[j].tareid
                                }

                                features.push(feature)
                            }
                        }
                    }

                    let geojson = {
                        type: "FeatureCollection",
                        features: features
                    }

                    this.cargarMapa(geojson);

                } else{

                    this.cargarMapa();
                }
            }

        },
        gestionObjetivo(){


        }
    }
})