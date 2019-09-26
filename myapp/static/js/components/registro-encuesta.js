let registroEncuesta = new Vue({
    el: "#registro-encuesta",
    delimitters: ['[[', ']]'],
    mounted(){

        var mymap = L.map('map',  {
            center: [51.505, -0.09],
            drawControl: true,
            zoom: 13
        });

        L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibmV1cm9tZWRpYSIsImEiOiJjazExNHZiaWQwNDl1M2Vxc3I5eWo2em5zIn0.UBBEXWDurA8wHC8-8DjdwA',
        {
            attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
            maxZoom: 18,
            id: 'mapbox.streets',
            accessToken: 'pk.eyJ1IjoibmV1cm9tZWRpYSIsImEiOiJjazExNHZiaWQwNDl1M2Vxc3I5eWo2em5zIn0.UBBEXWDurA8wHC8-8DjdwA'
        }).addTo(mymap);

        var drawnItems = new L.FeatureGroup();

        mymap.addLayer(drawnItems);

         var drawControl = new L.Control.Draw({
             edit: {
                 featureGroup: drawnItems
             }
         });

        mymap.addControl(drawControl);

        var toolbar = L.Toolbar();
        toolbar.addToolbar(map);

        /*var polygon = L.polygon([
            [51.10, -0.10],
            [51.10, -0.50],
            [51.50, -0.50],
            [51.50, -0.10]
        ]).addTo(mymap);*/
    },
    data: {

    }
})