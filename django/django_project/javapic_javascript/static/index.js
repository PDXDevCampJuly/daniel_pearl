/*-------------------------Create variables-------------------------*/

var jumbotron = document.getElementById("jumbotron");
var count = 1;

/*-------------------------Create slideshow-------------------------*/

function update_jumbotron(){
    //Creates a slideshow of photos

        if (count < 10){
            jumbotron.style.backgroundImage = "url(\"../static/images/pdxcg_0" + count + ".jpg\")"; //Loads images between 1 & 9
        } else {
            jumbotron.style.backgroundImage = "url(\"../static/images/pdxcg_" + count + ".jpg\")"; //loads images after 9
        }
        if (count == 60){
            count = 1; //Resets timer when all the pictures have been displayed
        } else {
            count += 1; //Increments the pictures
        }
}

setInterval(update_jumbotron, 5000);
