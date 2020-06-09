
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
      const first =  data.name.first;
      const last = data.name.last;
      const picture = data.picture.thumbnail;
      const city = data.location.city;
      const country = data.location.country;
      const state = data.location.state;
      const latitude = data.location.coordinates.latitude;
      const longitude = data.location.coordinates.longitude;
      
      
      L.marker([latitude,longitude]).addTo(mymap)
      .bindPopup(
        `<center> <p> <b> ${first} ${last} </b> <br><br> <img src = "${picture}"/> <br><br> ${city}, ${state}, ${country}  </p></center>`
      )
      .openPopup();
    }

}).catch((err) => console.log(err));






