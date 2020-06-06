
let mymap = L.map('mapid').setView([35.689722, 139.692222], 12);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw'
}).addTo(mymap);
        
const url = 'https://randomuser.me/api/?results=50'


axios.get(url)
  .then((response) => {

    for (i = 0; i < 11; i++) {
      const data = response.data.results[i];
      const name =  data.name
      const picture = data.picture
      const location = data.location
      const latitude = data.location.coordinates.latitude
      const longitude = data.location.coordinates.longitude
      
      L.marker([latitude,longitude]).addTo(mymap)
      .bindPopup('TEXT HERE')
      .openPopup();
    }

}).catch((err) => console.log(err));






