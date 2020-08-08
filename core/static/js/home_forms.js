$(document).ready(function(){
   $("#recommendationForm").submit(function(e){

      	e.preventDefault();

      	var serializedData = $(this).serialize();
      	$.ajax({
      		type : $(this).attr('method'),
      		url :  $(this).attr('action'),
      		data : serializedData,
      		success : function(data){
      			$('#sidebar-contact-reco').removeClass('sidebar-contact-reco-activated')
			   	$('div.overlay').css('z-index', -999).css('opacity', 0)
			   	$('html').css('overflow-y', 'visible')
      			$("#recommendationForm")[0].reset();
      		},
			/*
      		error : function(response){
      			console.log(response)
      		}
      		*/
      	});
   });

   $("#contactForm").submit(function(e){

      	e.preventDefault();

      	var serializedData = $(this).serialize();
      	$.ajax({
      		type : $(this).attr('method'),
      		url :  $(this).attr('action'),
      		data : serializedData,
      		success : function(data){
				$('#sidebar-contact-reco').removeClass('sidebar-contact-reco-activated')
			   	$('div.overlay').css('z-index', -999).css('opacity', 0)
			   	$('html').css('overflow-y', 'visible')
      			$("#contactForm")[0].reset();
      		},
      	});
   });
});