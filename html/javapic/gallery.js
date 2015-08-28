var gallery = document.getElementById("gallery");
//Sets gallery to the gallery id in html

var images = new Array();

function create_gallery(){
    //Creates a photo gallery that allows for resizing

    for (var i = 1; i < 60; i++){

        var new_list = document.createElement('li'); //creates new list
        var new_image = document.createElement('img'); //creates new image

        if (i < 10){
            new_image.src = "images/pdxcg_0" + i + ".jpg";
        } else {
            new_image.src = "images/pdxcg_" + i + ".jpg";
        }

        new_list.appendChild(new_image); //append images to list
        gallery.appendChild(new_list); //append lists to gallery
    }
}

create_gallery()
