let tarea = new Vue({
    delimiters: ['[[', ']]'],
    el: '#gestion-tareas',
    created(){

        if(window.location.pathname == '/tareas/'){

            this.listadoTareas();
            this.listadoProyectos();
            this.listadoInstrumentos();
        }
    },
    data: {
        tareas: [],
        edicionTarea: {},
        almacenamientoTarea: {},
        proyectos: [],
        instrumentos: [],
        loading: false,
        dimensionesTerritoriales: [],
        taskMap: {},
        dimensionTerritorialReferencia: {}
    },
    methods: {
        listadoTareas(){

            this.loader(true);

            axios({
                method: 'GET',
                url: '/tareas/list/',
                headers: {
                    Authorization: getToken()
                }
            })
            .then(response => {

                this.loader(false);

                if(response.data.code == 200 && response.data.status == 'success'){

                    this.tareas = response.data.tareas;
                }
            });
        },
        almacenarTarea(){

            this.loader(true);

            var queryString = Object.keys(this.almacenamientoTarea).map(key => {

                if(key == 'dimensionid'){

                    valor = this.almacenamientoTarea['dimensionid'].dimensionid;

                } else{

                    valor = this.almacenamientoTarea[key];
                }

                return key + '=' + valor;
            }).join('&');

            axios({
                method: 'post',
                url: '/tareas/store/',
                data: queryString,
                headers: {
                    'Content-type': 'application/x-www-form-urlencoded',
                    Authorization: getToken()
                }
            })
            .then(response => {

                $("#agregar-tarea").modal('hide')
                this.almacenamientoTarea = {};
                this.listadoTareas();

                this.loader(false);

                Swal.fire({
                  title: 'Exito!',
                  text: 'Tarea creada satisfactoriamente',
                  type: 'success',
                  confirmButtonText: 'Acepto'
                });
            })
            .catch(response => {

                $("#agregar-tarea").modal('hide')
                this.almacenamientoTarea = {};

                this.loader(false);

                Swal.fire({
                  title: 'Error!',
                  text: 'Ocurrio un error. Por favor intenta de nuevo',
                  type: 'error',
                  confirmButtonText: 'Acepto'
                });
            });
        },
        eliminarTarea(id){

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

                this.loader(true);

                axios({
                    method: 'DELETE',
                    url: '/tareas/delete/' + id,
                    headers: {
                        Authorization: getToken()
                    }
                })
                .then(response => {

                    this.loader(false);

                    this.listadoTareas();

                    Swal.fire(
                      'Eliminado!',
                      'La tarea fue eliminada de forma exitosa',
                      'success'
                    );
                })
                .catch(response => {

                     this.listadoTareas();

                     this.loader(false);

                     Swal.fire(
                      'Error!',
                      'Ocurrio un error por favor intenta de nuevo',
                      'error'
                    );
                });
              }
            });
        },
        editarTarea(){

            this.loader(true);

            var queryString = Object.keys(this.edicionTarea).map(key => {

                let valor = "";

                if(key == 'tarerestricgeo' && typeof this.edicionTarea.tarerestricgeo == 'object'){

                    valor = JSON.stringify(this.edicionTarea.tarerestricgeo);

                } else if(key == 'tarerestrictime' && typeof this.edicionTarea.tarerestrictime == 'object'){

                    valor = JSON.stringify(this.edicionTarea.tarerestrictime);

                } else{

                    valor = this.edicionTarea[key];
                }

                return key + '=' + valor;

            }).join('&');

            axios({
                method: 'post',
                url: '/tareas/' + this.edicionTarea.tareid,
                data: queryString,
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    Authorization: getToken()
                }
            })
            .then(response => {

                $("#editar-tarea").modal('hide');
                this.listadoTareas();
                this.loader(false);

                Swal.fire(
                    'Exito!',
                    'Tarea modificada satisfactoriamente',
                    'success'
                );
            })
            .catch(() => {

                $("#editar-tarea").modal('hide');
                this.loader(false);

                Swal.fire(
                    'Error!',
                    'Ocurrio un error. Por favor intenta de nuevo',
                    'error'
                );
            });
        },
        listadoProyectos(){

            axios({
                method: 'GET',
                url: '/proyectos/list/',
                headers: {
                    Authorization: getToken()
                }
            })
            .then(response => {

                if(response.data.code == 200 && response.data.status == 'success'){

                    this.proyectos = response.data.proyectos;
                }
            });
        },
        listadoInstrumentos(){

            axios({
                method: 'GET',
                url: '/instrumentos/list/',
                headers: {
                    Authorization: getToken()
                }
            })
            .then(response => {

              this.instrumentos = response.data;
            });
        },
        loader(status){

            this.loading = status;
        },
        obtenerDimensionesTerritoriales(proyid){

            axios({
                url: '/proyectos/dimensiones-territoriales/' + proyid,
                method: 'GET',
                headers: {
                    Authorization: getToken()
                }
            })
            .then(response => {

                if(response.data.code == 200 && response.data.status == 'success'){

                    this.dimensionesTerritoriales = response.data.dimensionesTerritoriales;
                }
            })
        },
        generarMapa(timeout, dimension){

            window.setTimeout(() => {

                var taskMap = L.map('taskmap',  {
                center: [3.450572, -76.538705],
                drawControl: false,
                zoom: 13
            });

                L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibmV1cm9tZWRpYSIsImEiOiJjazExNHZiaWQwNDl1M2Vxc3I5eWo2em5zIn0.UBBEXWDurA8wHC8-8DjdwA',
                {
                    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
                    maxZoom: 18,
                    id: 'mapbox.streets',
                    accessToken: 'pk.eyJ1IjoibmV1cm9tZWRpYSIsImEiOiJjazExNHZiaWQwNDl1M2Vxc3I5eWo2em5zIn0.UBBEXWDurA8wHC8-8DjdwA'
                }).addTo(taskMap);

                if(dimension){

                    this.dimensionTerritorialReferencia = L.polygon(this.obtenerCoordenadas(dimension.geojson)).addTo(taskMap);

                    //L.marker([3.45000, -76.535000]).addTo(taskMap);

                    var editableLayers = new L.FeatureGroup();

                    taskMap.addLayer(editableLayers);

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

                    taskMap.addControl(drawControl);

                    taskMap.on(L.Draw.Event.CREATED, (e) => {
                        type = e.layerType;
                        layer = e.layer;

                        if (type === 'polygon' && this.cantidadAreasMapa(editableLayers) == 0 && this.validarSubconjunto(layer.toGeoJSON())) {

                            editableLayers.addLayer(layer);
                            this.almacenamientoTarea.geojson_subconjunto = JSON.stringify(layer.toGeoJSON())
                            //this.almacenamientoInstrumento.areaInteres = layer.toGeoJSON();
                        }
                    });

                    taskMap.on(L.Draw.Event.DELETED, (e) => {

                        this.almacenamientoTarea.geojson_subconjunto = null;
                    });
                }

                this.taskMap = taskMap;
            }, timeout);
        },
        cantidadAreasMapa(editableLayers){

            return Object.keys(editableLayers._layers).length;
        },
        obtenerCoordenadas(geojson){

            coordenadas = [],

            coordenadasGeojson = JSON.parse(geojson).geometry.coordinates[0];

            for(let i=0; i < coordenadasGeojson.length; i++){

                coordenadas.push(coordenadasGeojson[i].reverse())
            }

            return coordenadas;
        },
        generarDimensionTerritorial(dimension){

            this.taskMap.remove();
            this.generarMapa(0, dimension);
        },
        validarSubconjunto(geojson){

            coordsFails = 0;

            var polyPoints = this.dimensionTerritorialReferencia.getLatLngs()[0];

            coordenadas = this.obtenerCoordenadas(JSON.stringify(geojson));
            console.log(coordenadas);

            for(var k = 0; k < coordenadas.length; k++){

                var x = coordenadas[k][0], y = coordenadas[k][1];

                var inside = false;
                for (var i = 0, j = polyPoints.length - 1; i < polyPoints.length; j = i++) {
                    var xi = polyPoints[i].lat, yi = polyPoints[i].lng;
                    var xj = polyPoints[j].lat, yj = polyPoints[j].lng;

                    var intersect = ((yi > y) != (yj > y))  && (x < (xj - xi) * (y - yi) / (yj - yi) + xi);
                    if (intersect) inside = !inside;
                }

                if(!inside){
                    coordsFails++
                };
            }

            if(coordsFails > 0){

                return false;

            } else{

                return true;
            }
        }
    },
    filters: {
        tipoTarea(value){

            if(value == 1){

                return "Encuesta";

            } else if(value == 2){

                return "Cartografia";
            }
        }
    }
})