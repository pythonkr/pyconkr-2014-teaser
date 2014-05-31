var pyconKr = (function($) {
		var $body = $('body'),
		$window = $(window),
		doc = document,
		$link = $('#nav').find('a'),
        scrollAnchor, scrollPoint,
        map, eventLocationMarker;

	function init() {
		$link.on('click', function() {
			scrollAnchor = $(this).attr('data-scroll');
            scrollPoint = $('section[data-anchor="' + scrollAnchor + '"]').offset().top - 28;

            $('body,html').animate({
                scrollTop: scrollPoint
            }, 500);

            return false;
        });

        // google maps
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
	}

	return {
		init: init
	};
})(jQuery);

$(document).ready(function() {
	pyconKr.init();
});

