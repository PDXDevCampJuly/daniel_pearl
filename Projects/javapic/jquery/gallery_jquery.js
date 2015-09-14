/*-------------------------Create variables-------------------------*/

var gallery = document.getElementById("gallery");
var image_show = document.getElementById("image_show");
var tagline = document.querySelector(".tagline");
var name_input = sessionStorage.getItem("name_input");

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
    }
}

create_gallery();

/*----------------------Change Name in Tagline----------------------*/

if (name_input !== ""){
    tagline.innerHTML = "develop something beautiful, " + name_input;
} else{
    tagline.innerHTML = "develop something beautiful";
}

/*----------------------Enlarge & hide images----------------------*/

$("#image_show").click(function(){ //hide
    if(this.children[0].nodeName === "IMG"){
        $("#image_show").toggleClass("display_none display_img");
    }
});

$(".gallery img").click(function(){ //enlarge image
    $("#image_show img").attr("src", this.src);
    $("#image_show").toggleClass("display_none display_img");
});
