let informacionEncuesta = new Vue({
    el: '#gestion-informacion-encuesta',
    delimiters: ['[[', ']]'],
    created(){

        if(window.location.pathname.substr(1, 24) == "instrumentos/informacion"){

            this.instrumentoID = window.location.pathname.substr(26, 36);
            this.listadoInformacion()
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
        listadoInformacion(id){

            axios({
                method: 'GET',
                url: '/instrumentos/' + this.instrumentoID + '/informacion/',
                headers:{
                    Authorization: getToken()
                }
            })
            .then(response => {

                if(response.data.code == 200 && response.data.info.info.length > 0){

                    this.informacion = response.data.info.info;

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
                }
            })
        }
    }
});