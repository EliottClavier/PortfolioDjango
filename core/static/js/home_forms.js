$(document).ready(function(){
   $("#recommendationForm").submit(function(e){

      	e.preventDefault();

      	var serializedData = $(this).serialize();
      	$.ajax({
      		type : $(this).attr('method'),
      		url :  $(this).attr('action'),
      		data : serializedData,
      		success : function(data){
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

      			$("#contactForm")[0].reset();
      		},
      	});
   });
});