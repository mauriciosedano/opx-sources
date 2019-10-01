let informacionEncuesta = new Vue({
    el: '#gestion-informacion-encuesta',
    delimiters: ['[[', ']]'],
    created(){

        if(window.location.pathname.substr(1, 24) == "instrumentos/informacion"){

            this.instrumentoID = window.location.pathname.substr(26, 36);
            this.informacionInstrumento();
        }
    },
    data:{
        informacion: [],
        instrumentoID: 0,
        camposIgnorados: [
            "_notes",
            "meta/instanceID",
            "end",
            "start",
            "_submission_time",
            "_uuid",
            "_bamboo_dataset_id",
            "_tags",
            "_attachments",
            "_submitted_by",
            "_geolocation",
            "_validation_status",
            "_xform_id_string",
            "_status",
            "_id",
            "__version__",
            "formhub/uuid"
        ],
        camposInformacion: []
    },
    methods: {
        informacionInstrumento(id){

            axios({
                method: 'GET',
                url: '/instrumentos/' + this.instrumentoID + '/informacion/',
                headers:{
                    Authorization: getToken()
                }
            })
            .then(response => {

                if(response.data.code == 200 && response.data.status == 'success'){

                    if(response.data.info['tipoInstrumento'] == 1){

                        this.informacionEncuesta(response.data.info);

                    } else if(response.data.info['tipoInstrumento'] == 2){

                        this.informacionCartografia(response.data.info);
                    }
                }


            })
        },
        informacionEncuesta(info){

            this.informacion = info.info;

            // Captura de campos de interés
            let camposTotales = Object.keys(this.informacion[0])

            for(let i = 0; i < camposTotales.length; i++){

                let matchs = 0

                for(let j = 0; j < this.camposIgnorados.length; j++){

                    if(camposTotales[i] == this.camposIgnorados[j]){

                        matchs++;
                    }

                    if(j == this.camposIgnorados.length - 1 && matchs == 0){

                        this.camposInformacion.push(camposTotales[i])
                    }
                }

            }
        },
        informacionCartografia(info){

            console.log(info);
            /*{
                center: ,
                drawControl: false,
                zoom: 13
            }*/

            var mymap = L.map('tmmap').setView([3.450572, -76.538705], 13);

            L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibmV1cm9tZWRpYSIsImEiOiJjazExNHZiaWQwNDl1M2Vxc3I5eWo2em5zIn0.UBBEXWDurA8wHC8-8DjdwA',
            {
                attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
                maxZoom: 18,
                id: 'mapbox.streets',
                accessToken: 'pk.eyJ1IjoibmV1cm9tZWRpYSIsImEiOiJjazExNHZiaWQwNDl1M2Vxc3I5eWo2em5zIn0.UBBEXWDurA8wHC8-8DjdwA'
            }).addTo(mymap);

            let coordenadasTM = info.areaOfInterest.coordinates[0][0];
            let coordenadas = [];

           for(let i = 0; i < coordenadasTM.length; i++){

            coordenadas.push(coordenadasTM[i].reverse());
           }

           console.log(coordenadas);

            var polygon = L.polygon(coordenadas).addTo(mymap);

        }
    }
});