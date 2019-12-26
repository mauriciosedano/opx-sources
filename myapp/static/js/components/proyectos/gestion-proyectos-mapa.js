gestionProyecto = new Vue({
    el: '#gestion-proyectos-mapa',
    delimiters: ['[[', ']]'],
    data: {
        informacionProyecto: {},
        map: {},
        proyectos: [],
        proyectoGestion: {},
        tareaGestion: {},
        capaEdicion: '',
        acciones: {
            objetivo: false,
            tiempo: false,
            territorio: false
        },
        gestionTerritorial: {
            areaDimensionTerritorial: true,
            listadoTareas: false,
            areaTarea: false
        },
        datosCambioTerritorial: {
            geojson: false,
            tareas: []
        }
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
                        onEachFeature: (feature, layer) => {

                            layer.on('click', () => {

                                this.capaEdicion = feature.properties;

                                if(feature.properties.type == 'dimension'){

                                    this.acciones.objetivo = false;
                                    this.acciones.tiempo = true;
                                    this.acciones.territorio = true;

                                } else if(feature.properties.type == 'tarea'){

                                    this.acciones.objetivo = true;
                                    this.acciones.tiempo = false;
                                    this.acciones.territorio = false;
                                }
                            });
                        },
                        style: (feature) => {

                            return {color: feature.properties.color}
                        }
                    })
                    .bindPopup(function (layer) {
                        return layer.feature.properties.description;
                    })
                    .addTo(this.map)
                }
            }, 1000);

        },
        cargarMapaGestionTerritorial(){

            map = L.map('mapa-dimension-territorial',  {
                center: [3.450572, -76.538705],
                drawControl: false,
                zoom: 13
            });

            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
              attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
            }).addTo(map);

            L.tileLayer.wms('http://ws-idesc.cali.gov.co:8081/geoserver/wms?service=WMS', {
              layers: 'idesc:mc_barrios',
              format: 'image/png',
              transparent: !0,
              version: '1.1.0'
            }).addTo(map);

            var editableLayers = new L.FeatureGroup();

            map.addLayer(editableLayers);

            var options = {
                // position: 'topright',
                draw: {
                    polygon: {
                        allowIntersection: true, // Restricts shapes to simple polygons
                        drawError: {
                            color: '#e1e100', // Color the shape will turn when intersects
                            message: '<strong>Oh snap!</strong> you can\'t draw that!' // Message that will show when intersect
                        },
                        shapeOptions: {
                            color: '#0CBAEF'
                        }
                    },
                    polyline: false,
                    circle: false, // Turns off this drawing tool
                    rectangle: false,
                    marker: false,
                    circlemaker: false
                },
                edit: {
                    featureGroup: editableLayers, //REQUIRED!!
                    //remove: false
                }
            };

            var drawControl = new L.Control.Draw(options);

            map.addControl(drawControl);

            map.on(L.Draw.Event.CREATED, (e) => {
                type = e.layerType;
                layer = e.layer;

                if (type === 'polygon' && this.cantidadAreasMapa(editableLayers) == 0) {

                    editableLayers.addLayer(layer);

                    this.datosCambioTerritorial['geojson'] = JSON.stringify(layer.toGeoJSON());
                }
            });

            map.on(L.Draw.Event.DELETED, (e) => {

                 if(this.cantidadAreasMapa(editableLayers) == 0){

                    this.cambioTerritorial.geojson = null;
                 }
            });
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
                            color: '#0CBAEF',
                            description: dimensiones[i].nombre,
                            dimensionid: dimensiones[i].dimensionid,
                            id: dimensiones[i].proyid,
                            type: 'dimension'
                        }

                        features.push(feature)

                        tareas = dimensiones[i].tareas;
                        cantidadTareas = dimensiones[i].tareas.length;

                        if(cantidadTareas > 0){

                            for(let j=0; j<cantidadTareas; j++){

                                let feature = JSON.parse(tareas[j].geojson_subconjunto)
                                feature.properties = {
                                    color: '#F4B821',
                                    description: tareas[j].tarenombre,
                                    id: tareas[j].tareid,
                                    type: 'tarea'
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
        gestionTiempoProyecto(){

            axios({
                url: '/proyectos/detail/' + this.capaEdicion.id,
                headers: {
                    Authorization: getToken()
                }
            })
            .then(response => {

                if(response.data.code == 200 && response.data.status == 'success'){

                    this.proyectoGestion = response.data.detail.proyecto;
                    this.proyectoGestion['proyid'] = this.capaEdicion.id;
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
        },
        gestionTerritorioProyecto(){

            this.obtenerTareasDimensionTerritorial();

            $("#gestion-territorio-proyecto").modal({
                backdrop: 'static',
                show: true
            });

           window.setTimeout(() => {
            this.cargarMapaGestionTerritorial();
           }, 1000);
        },
        paso2GestionTerritorial(){

            this.gestionTerritorial.areaDimensionTerritorial = false;
            this.gestionTerritorial.listadoTareas = true;
            this.areaTarea = false;
        },
        obtenerTareasDimensionTerritorial(){

            axios({
                url: '/tareas-dimension-territorial/' + this.capaEdicion.dimensionid,
                method: 'GET',
                headers: {
                    Authorization: getToken()
                }
            })
            .then(response => {

                this.datosCambioTerritorial.tareas = response.data.data;
            });
        },
        gestionObjetivoProyecto(){

            axios({
                url: '/tareas/detail/' + this.capaEdicion.id,
                headers: {
                    Authorization: getToken()
                }
            })
            .then(response => {

                console.log(response);

                if(response.data.code == 200 && response.data.status == 'success'){

                    this.tareaGestion = response.data.tarea;
                    this.tareaGestion['tareid'] = this.capaEdicion.id;
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
        },
        edicionObjetivoTarea(){

            queryString = Object.keys(this.tareaGestion).map(key => {

                return key + '=' + this.tareaGestion[key];
            })
            .join('&');

            axios({
                url: '/tareas/' + this.tareaGestion.tareid,
                method: 'POST',
                data: queryString,
                headers: {
                 'Content-Type': 'application/x-www-form-urlencoded',
                 Authorization: getToken()
                }
            })
            .then(response => {

                if(response.data.code == 200 && response.data.status == 'success'){

                    $("#gestion-objetivo-tarea").modal('hide');

                    Swal.fire({
                        title: 'Exito',
                        text: 'El Objetivo fue cambiado de forma satisfactoria',
                        type: 'success'
                    });
                }
            })
            .catch(() => {

                $("#gestion-objetivo-tarea").modal('hide');

                Swal.fire({
                    title: 'Error',
                    text: 'Ocurrio un error. Por favor intenta de nuevo.',
                    type: 'error'
                });
            });
        },
        edicionTiempoProyecto(){

        queryString = Object.keys(this.proyectoGestion).map(key => {

                return key + '=' + this.proyectoGestion[key];
            })
            .join('&');

        axios({
            url: '/proyectos/' + this.proyectoGestion.proyid,
            method: 'POST',
            data: queryString,
            headers: {
             'Content-Type': 'application/x-www-form-urlencoded',
             Authorization: getToken()
            }
        })
        .then(response => {

            $("#gestion-proyecto").modal('hide');

            Swal.fire({
                title: 'Exito',
                text: 'El Objetivo fue cambiado de forma satisfactoria',
                type: 'success'
            });
        })
        .catch(() => {

            $("#gestion-proyecto").modal('hide');

            Swal.fire({
                title: 'Error',
                text: 'Ocurrio un error. Por favor intenta de nuevo.',
                type: 'error'
            });
        });
    },
        cantidadAreasMapa(editableLayers){

            return Object.keys(editableLayers._layers).length;
        }
    }
})