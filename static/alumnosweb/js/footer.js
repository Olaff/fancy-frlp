//Ensure sticky footer plus a "Top button"

$(document).ready(function() {

	var docHeight = $(window).height();
	var footerHeight = $('#footer').height();
	var footerTop = $('#footer').position().top + footerHeight;
			
	if (footerTop < docHeight) {
		$('#footer').css('margin-top', 10 + (docHeight - footerTop) + 'px');
	}
			
	$('#jumpback').click(function () {
		$('body,html').animate({
			scrollTop: 0
		}, 800);
				
	return false;
	});
});
