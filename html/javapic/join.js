
var gallery = document.getElementById("gallery");
//Sets gallery to the gallery id in html
var jumbotron = document.getElementById("jumbotron")

var images = new Array();

function create_gallery(){
    //Creates a photo gallery that allows for resizing

    for (var i = 1; i < 60; i++){

        var new_list = document.createElement('li');
        var new_image = document.createElement('img');

        if (i < 10){
            new_image.src = "images/pdxcg_0" + i + ".jpg";
        } else {
            new_image.src = "images/pdxcg_" + i + ".jpg";
        }
        new_list.appendChild(new_image);
        gallery.appendChild(new_list);
    }
    //gallery.addEventListener('click', resize;
}

function create_jumbotron(){
    //Creates a slideshow of photos

    for (var i = 0; i < 10; i++){

        var new_image = document.createElement('img');

        new_image.src = "images/pdxcg_0" + i + ".jpg";
        new_list.appendChild(new_image);
        gallery.appendChild(new_list);
    }
}
function resize(){
    gallery.appendChild(new_list);
}

create_gallery()
