proyecto = new Vue({
     el: '#gestion-proyectos',
    delimiters: ['[[', ']]'],
    created: function(){

        this.listadoProyectos();
    },
    data: {
        proyectos: [],
        almacenamientoProyecto: {}
    },
    methods: {
        listadoProyectos: function(){

            axios.get('/proyectos/').then(response => {

                this.proyectos = response.data;
                console.log(this.proyectos);
            })
        }
    }
})