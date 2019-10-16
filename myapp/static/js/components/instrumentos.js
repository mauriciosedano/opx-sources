let instrumento = new Vue({
    delimiters: ['[[', ']]'],
    el: '#gestion-instrumentos',
    created(){

        if(window.location.pathname == '/instrumentos/'){

            this.listadoInstrumentos();
        }
    },
    data: {
        instrumentos: [],
        almacenamientoInstrumento: {},
        edicionInstrumento: {},
        fase1: true,
        fase2Cartografia: false,
        allowRegister: false,
        loading: false
    },
    methods: {
        listadoInstrumentos(){

            this.loader(true);

            axios({
                method: 'GET',
                url: '/instrumentos/list/',
                headers: {
                    Authorization: getToken()
                }
            })
            .then(response => {

              this.instrumentos = response.data;
              this.loader(false);
            });
        },
        prepararInstrumento(){

            if(this.almacenamientoInstrumento.instrtipo == "1"){

            } else if(this.almacenamientoInstrumento.instrtipo == "2"){

                this.fase1 = false;
                this.fase2Cartografia = true;

                window.setTimeout(() => {
                    this.cargarMapaRegistro();
                }, 1000);
            }
        },
        almacenarInstrumento(){

            this.loader(true);

            var queryString = Object.keys(this.almacenamientoInstrumento).map(key => {

                if(key == 'areaInteres'){

                    return key + "=" + JSON.stringify(this.almacenamientoInstrumento[key])

                } else{

                    return key + '=' + this.almacenamientoInstrumento[key];
                }

            }).join('&');

            axios({
                method: 'post',
                url: '/instrumentos/store/',
                data: queryString,
                headers: {
                    'Content-type': 'application/x-www-form-urlencoded',
                    Authorization: getToken()
                }
            })
            .then(response => {

                $("#agregar-instrumento").modal('hide')
                this.almacenamientoInstrumento = {};
                this.listadoInstrumentos();

                this.fase1 = true;
                this.fase2Cartografia = false;
                this.allowRegister = false;

                this.loader(false);

                Swal.fire({
                  title: 'Exito!',
                  text: 'Instrumento creado satisfactoriamente',
                  type: 'success',
                  confirmButtonText: 'Acepto'
                });
            })
            .catch(response => {

                $("#agregar-instrumento").modal('hide')
                this.almacenamientoInstrumento = {};

                this.fase1 = true;
                this.fase2Cartografia = false;
                this.allowRegister = false;

                this.loader(false);

                Swal.fire({
                  title: 'Error!',
                  text: 'Ocurrio un error. Por favor intenta de nuevo',
                  type: 'error',
                  confirmButtonText: 'Acepto'
                });
            });
        },
        eliminarInstrumento(id){

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
                    url: '/instrumentos/delete/' + id,
                    headers: {
                        Authorization: getToken()
                    }
                })
                .then(response => {

                    this.listadoInstrumentos();

                    this.loader(false);

                    Swal.fire(
                      'Eliminado!',
                      'El instrumento fue eliminado de forma exitosa',
                      'success'
                    );
                })
                .catch(response => {

                     this.listadoInstrumentos();

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
        editarInstrumento(){

            this.loader(true);

            var queryString = Object.keys(this.edicionInstrumento).map(key => {

                return key + '=' + this.edicionInstrumento[key];

            }).join('&');

            axios({
                method: 'post',
                url: '/instrumentos/' + this.edicionInstrumento.instrid,
                data: queryString,
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    Authorization: getToken()
                }
            })
            .then(response => {

                $("#editar-instrumento").modal('hide');
                this.listadoInstrumentos();
                this.loader(false);

                Swal.fire(
                    'Exito!',
                    'Instrumento modificado satisfactoriamente',
                    'success'
                );
            })
            .catch(() => {

                $("#editar-instrumento").modal('hide');
                this.loader(false);

                Swal.fire(
                    'Error!',
                    'Ocurrio un error. Por favor intenta de nuevo',
                    'error'
                );
            });
        },
        verificarImplementacionEncuesta(id){

            return new Promise((resolve, reject) => {

                axios({
                    method: 'GET',
                    url: '/instrumentos/' + id + '/verificar-implementacion/',
                    headers: {
                        Authorization: getToken()
                    }
                })
                .then(response => {

                    if(response.data.code == 200){

                        resolve(response.data.implementacion);
                    }
                })
                .catch(response => {

                    reject(false);
                });

            });
        },
        async implementarEncuesta(id){

            this.loader(true);

            await this.verificarImplementacionEncuesta(id)
            .then(response => {

                if(!response){

                    axios({
                        method: 'GET',
                        url: '/instrumentos/' + id + '/implementar/',
                        headers: {
                            Authorization: getToken()
                        }
                    })
                    .then(response => {

                        this.loader(false);

                        Swal.fire({
                            title: 'Exito',
                            text: 'La encuesta fue implementada exitosamente',
                            type: 'success'
                        });

                    })
                    .catch( error => {

                        this.loader(false);

                        Swal.fire({
                            title: 'Error',
                            text: 'Ocurrio un error. Por favor intenta de nuevo',
                            type: 'error'
                        });
                    });

                } else{

                    this.loader(false);

                    Swal.fire({
                        title: 'Implementado',
                        text: 'El instrumento ya se encuentra implementado',
                        type: 'warning'
                    });
                }
            })
            .catch( error => {

                this.loader(false);

                Swal.fire({
                    title: 'Error',
                    text: 'Ocurrio un error. Por favor intenta de nuevo',
                    type: 'error'
                });
            })
        },
        async informacionEncuesta(id){

            this.loader(true);

            await this.verificarImplementacionEncuesta(id)
            .then(response => {

                if(response){

                    location.href = '/instrumentos/informacion/' + id;

                } else{

                    this.loader(false);

                    Swal.fire({
                        title: 'Error',
                        text: 'El formulario no se encuentra implementado',
                        type: 'error'
                    });
                }
            })
            .catch(error => {

                this.loader(false);

                Swal.fire({
                    title: 'Error',
                    text: 'Ocurrio un error. Por favor intenta de nuevo',
                    type: 'warning'
                });
            });
        },
        cargarMapaRegistro(){

            var mymap = L.map('tmmap',  {
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
            }).addTo(mymap);

            var editableLayers = new L.FeatureGroup();

            mymap.addLayer(editableLayers);

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

            mymap.addControl(drawControl);

            mymap.on(L.Draw.Event.CREATED, (e) => {
                type = e.layerType;
                layer = e.layer;

                if (type === 'polygon' && this.cantidadAreasMapa(editableLayers) == 0) {

                    editableLayers.addLayer(layer);
                    this.almacenamientoInstrumento.areaInteres = layer.toGeoJSON();
                }

                if(this.cantidadAreasMapa(editableLayers) == 1){

                    this.allowRegister = true;
                }
            });

            mymap.on(L.Draw.Event.DELETED, (e) => {

                if(this.cantidadAreasMapa(editableLayers) == 0){

                    this.allowRegister = false;
                }
            });

        },
        cantidadAreasMapa(editableLayers){

            return Object.keys(editableLayers._layers).length;
        },
        loader(status){

            this.loading = status;
        }
    },
    filters: {
        tipoInstrumento(value){

            if(value == 1){

                return "Encuesta";

            } else if(value == 2){

                return "Cartografía";
            }
        }
    }
});