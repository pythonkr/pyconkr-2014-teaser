// google maps

var map;
var eventLocationMarker;

google.maps.event.addDomListener(window, 'load', function() {
    eventLocationMarker = new google.maps.Marker({
        // 잠실 롯데호텔월드
        position: new google.maps.LatLng(37.511453, 127.100181)
    });
    map = new google.maps.Map(document.getElementById('map-canvas'), {
        zoom: 15,
        center: eventLocationMarker.getPosition()
    });
    eventLocationMarker.setMap(map);
});
