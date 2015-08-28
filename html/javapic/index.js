//Sets gallery to the gallery id in html
var jumbotron = document.getElementById("jumbotron");
var count = 1;

function update_jumbotron(){
    //Creates a slideshow of photos

        if (count < 10){
            jumbotron.style.backgroundImage = "url(\"images/pdxcg_0" + count + ".jpg\")";
        } else {
            jumbotron.style.backgroundImage = "url(\"images/pdxcg_" + count + ".jpg\")";
        }

        if (count == 60){
            count = 1; //Resets timer when all the pictures have been displayed
        } else {
            count += 1; //Increments the picture #
        }
}



setInterval(update_jumbotron, 5000);
