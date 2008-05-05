var LWL;

if (!LWL) LWL = {};

/*
	Text used in the help tooltips for the form
*/
LWL.help = {
	body	:"The lyrics you would like to share",
	artist	:"The artist who wrote these lyrics",
	song	:"The song in which these lyrics appear",
	album	:"<strong>Optional.</strong> The album where the song appears",
	ASIN	:"<strong>Optional.</strong> The Amazon ASIN code for the album or song",
}


LWL.initFormHelp = function() {
	
	for (fieldname in LWL.help) {
		$("#"+fieldname+"-field").attr('title', LWL.help[fieldname]);
		$("#"+fieldname+"-field").inputHintBox({
												className:'tooltip',
												source:'attr',
												attr:'title',
												incrementLeft:100,
												incrementTop:37,
												attachTo:'#wrapper'});
	}
	
}