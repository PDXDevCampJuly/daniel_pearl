/*-------------------------Create variables-------------------------*/

var gallery = document.getElementById("gallery");
var image_show = document.getElementById("image_show");

/*---------------------Populate site with images---------------------*/

function create_gallery(){
    //Displays images on page that use gallery settings

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

        eventListeners();
    }
}
/*-----------------------Make Images Clickable-----------------------*/

function image_click(e){
    //Add target event
    image_change(e.target);
}

function image_change(select_image){
    //Change image display
    if (image_show.className === "display_img") { //removes image
        image_show.className = "display_none";
    } else if (image_show.className = "display_none"){ //reveals image
        image_show.firstElementChild.src= select_image.src;
        image_show.className = "display_img";
    }
}

/*------------------------Add Event Listeners------------------------*/

function eventListeners(){
    //Add click events to image
    gallery.addEventListener("click", image_click, false);
    image_show.addEventListener("click", image_change, false);
}

create_gallery();
