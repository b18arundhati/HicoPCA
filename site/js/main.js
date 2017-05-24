var file; 

$(function() {
	$("#hicoHeaderChooser").on('change',function(data) { 
		processHicoHdr(data) 
	});

	$("#filesetInfoBtn").click(onFileInfoClick); 

	$("#pcaBtn").click(getPCA); 
})

function processHicoHdr(data) {
	file = document.getElementById('hicoHeaderChooser').files[0]; 
	var filename = file.name; 

	$.ajax({
		url: '/setHicoFile',
		method: "GET",  
		data: { filename: filename }, 
		success: function(data) {
			console.log(data); 
		}, 
		error: function(err) {
			console.error(err); 
		}
	});
}

function getPCA() {
	$.ajax({
		url: '/getPCA',
		method: "GET",  
		success: function(data) {
			window.location = data; 
		}, 
		error: function(err) {
			console.error(err); 
		}
	});
}

function onFileInfoClick() {
	$.ajax({
		url: '/getHicoFile',
		method: "GET",  
		success: function(filebase) {
			showFileInfo(filebase + ".hico.hdr"); 
		}, 
		error: function(err) {
			console.error(err); 
		}
	});
}

function print(text) {
	window.open().document.write("<pre>" + text + "</pre>");
}

function showFileInfo(filename) {
	var reader = new FileReader();
	reader.readAsText(file, 'UTF-8');

	reader.onload = function() { print(reader.result) }; 
}