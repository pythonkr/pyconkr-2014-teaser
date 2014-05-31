var pyconKr = (function($) {
		var $body = $('body'),
		$window = $(window),
		doc = document,
		$link = $('#nav').find('a'),
        $mMenu = $('#m-menu'),
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

        $mMenu.on('click', function() {
            $body.toggleClass('active');
            return false;
        });

        // google maps
        google.maps.event.addDomListener(window, 'load', function() {
            eventLocationMarker = new google.maps.Marker({
                // 숙명여대
                position: new google.maps.LatLng(37.546171, 126.964662)
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

