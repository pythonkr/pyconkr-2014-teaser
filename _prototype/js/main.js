var pyconKr = (function($) {
		var $body = $('body'),
		$window = $(window),
		doc = document,
		$link = $('#nav').find('a');

	function init() {
		$link.on('click', function() {
			var scrollAnchor = $(this).attr('data-scroll'),
       		scrollPoint = $('section[data-anchor="' + scrollAnchor + '"]').offset().top - 28;

    		$('body,html').animate({
        		scrollTop: scrollPoint
    		}, 500);

    		return false;
		});
	}

	return {
		init: init
	};
})(jQuery);

$(document).ready(function() {
	pyconKr.init();
});