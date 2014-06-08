var WebFontConfig = {
    google: {
        families: ['Raleway:300,700,900,500:latin']
    }
};

(function () {
    var wf = document.createElement('script');
    wf.src = ('https:' == document.location.protocol ? 'https' : 'http') +
        '://ajax.googleapis.com/ajax/libs/webfont/1/webfont.js';
    wf.type = 'text/javascript';
    wf.async = 'true';
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(wf, s);
})();

$(document).ready(function() {
	$('body').css({
		fontFamily: "'Raleway', 'Segoe UI', 'Malgun Gothic', 'AppleGothic', 'Dotum', sans-serif",
		WebkitTextSizeAdjust: 'none',
		textRendering: 'optimizeLegibility',
		WebkitFontSmoothing: 'antialiased',
		fontSmooth: 'always'
	});

	$('#main h1').css({
		textShadow: '0 1px 0 rgba(0, 0, 0, 0.125)',
		fontFamily: 'Raleway',
		color: 'rgb(136, 153, 170)'
	}).html('PyCon Korea 2014<span>PYCON KOREA <b style="color: #E55">AUG</b> <b style="color:#55E">30th</b> in Seoul</span>');

	$('#main .cfp').css({
		display: 'block',
		margin: '0 auto',
		background: 'rgba(0, 0, 0, 0.375)',
		color: 'rgba(255, 255, 255, 0.8)',
		boxShadow: '0 1px 0 rgba(0, 0, 0, 0.5)'
	}).html('<span style="display: table-cell; width: 252px; height: 54px; vertical-align: middle; font-size: inherit; font-weight: inherit">' + $('#main .cfp').html() + '</span>').find('span span span').css({
		fontSize: '10pt',
		letterSpacing: '-1pt'
	});

	$('#main .cfp').mousedown(function() {
		$(this).css({
			background: 'rgba(0, 0, 0, 0.5)',
			boxShadow: '0 1px 0 rgba(0, 0, 0, 0.75)',
			color: 'rgb(255, 255, 255)'
		});
	}).mouseup(function() {
		$(this).css({
			background: 'rgba(0, 0, 0, 0.375)',
			color: 'rgba(255, 255, 255, 0.8)',
			boxShadow: '0 1px 0 rgba(0, 0, 0, 0.5)'
		});
	}).mouseenter(function() {
		$(this).css({
			background: 'rgba(0, 0, 0, 0.4375)',
			boxShadow: '0 1px 0 rgba(0, 0, 0, 0.625)',
			color: 'rgba(255, 255, 255, 0.9)'
		});
	}).mouseleave(function() {
		$(this).css({
			background: 'rgba(0, 0, 0, 0.375)',
			color: 'rgba(255, 255, 255, 0.8)',
			boxShadow: '0 1px 0 rgba(0, 0, 0, 0.5)'
		});
	});

	if($(window).width() >= 600) {
		$('div.contents.row.col-md-offset-3').height($('div.contents.row.col-md-offset-3').height()).css({
			position: 'relative',
			margin: 0
		}).find('div').css({
			position: 'absolute',
			top: 0
		}).eq(0).css('left', '25%');

		$('div.contents.row.col-md-offset-3 div').eq(1).css('right', '25%');
	}

	$('div.schedule.col-md-offset-4.col-md-4 dl').css('display', 'inline-block')

	$('footer p').html('Copyright &copy; Python Korea. All rights Reserved.');

	$(window).resize(function() {
		if($(window).width() < 600) {
			$('div.contents.row.col-md-offset-3').css('height', 'auto').find('div').css('position', 'static');
		} else {
			$('div.contents.row.col-md-offset-3').height($('div.contents.row.col-md-offset-3 div').height()).find('div').css('position', 'absolute');
		}
	});

	$('#cfp .schedule dl dt').css({
		marginRight: '30px',
		textAlign: 'right',
		width: 120
	});

	$('#cfp .schedule dl dd').css({
		width: 120,
		padding: 0,
		margin: 0,
		textAlign: 'left'
	});

	$('div.container-fluid p.email a').css({
		border: 'dashed 1px rgba(49, 33, 5, 0.5)',
		boxShadow: '0 1px 0 rgba(0, 0, 0, 0.125)',
		padding: '10px 15px',
		marginTop: '10px',
		display: 'inline-block',
		borderRadius:'10px'
	}).mouseenter(function() {
		$(this).css('background', 'rgba(255, 255, 255, 0.125)');
	}).mouseleave(function() {
		$(this).css('background', 'transparent');
	}).mousedown(function() {
		$(this).css('background', 'rgba(0, 0, 0, 0.125)');
	}).mouseup(function() {
		$(this).css('background', 'rgba(255, 255, 255, 0.125)');
	});
});