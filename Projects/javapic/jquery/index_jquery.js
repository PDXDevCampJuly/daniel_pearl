/*-------------------------Create variables-------------------------*/

var jumbotron = document.getElementById("jumbotron");
var count = 1;

/*-------------------------Create slideshow-------------------------*/

function update_jumbotron(){
    //Creates a slideshow of photos

    if (count < 10){
        $(".jumbotron").css("background-image", "url(\"images/pdxcg_0" + count + ".jpg\")");
    } else {
        $(".jumbotron").css("background-image", "url(\"images/pdxcg_" + count + ".jpg\")");
    }
    if (count == 60){
        count = 1; //Resets timer
    } else {
        count += 1; //Increments pictures
    }
}
setInterval(update_jumbotron, 5000);
