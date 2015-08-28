
var gallery = document.getElementById("gallery");

function create_gallery(){

    var new_list = document.createElement('li');
    
    var new_image = document.createElement('img');

    new_image.setAttribute("src", "images/pdxcg_01.jpg");
    new_image.setAttribute("width", "300");
    new_image.setAttribute("alt", "1st pick");
    gallery.appendChild(new_image);

}

create_gallery()
