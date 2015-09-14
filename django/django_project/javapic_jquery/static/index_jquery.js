/*-------------------------Create variables-------------------------*/

var count = 1;

/*-------------------------Create slideshow-------------------------*/

function update_jumbotron(){
    //Creates a slideshow of photos

    if (count < 10){
        $(".jumbotron").css("background-image", "url(\"../static/images/pdxcg_0" + count + ".jpg\")");
    } else {
        $(".jumbotron").css("background-image", "url(\"../static/images/pdxcg_" + count + ".jpg\")");
    }
    if (count == 60){
        count = 1; //Resets timer
    } else {
        count += 1; //Increments pictures
    }
}
setInterval(update_jumbotron, 5000);
