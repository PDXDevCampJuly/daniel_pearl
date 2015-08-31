/*-------------------------Create variables-------------------------*/

var name = document.getElementsByName("name");
var username = document.getElementsByName("username");
var email = document.getElementsByName("email");
var submit = document.getElementByName("submit");

/*--------------------------Validate Input--------------------------*/

function validation(){ // validates name is entered
    if (name.length === 0) {
        alert("You must enter a name.");
        return false;
    }
    if (userName.length === 0) { //validates userName is entered
        alert("You must enter a username.");
        return false;
    }
    if (email.length === 0) { //validates email is entered
        alert("You must enter an email.");
        return false;
    }
    return true;
}

/*----------------------Submit and Change name----------------------*/

function submit_form(){
    //submits form and returns to gallery page
    if (validation() === true){
        change_name();
        document.href = "gallery.html";
    }
}

function change_name(){
    //Changes name in gallery page
    document.getElementsByTagName("span").innerHTML = '"develop something beautiful,' +  name';
}
 
/*-----------------------Add Event Listeners-----------------------*/

submit.addEventListener("click", submit_form, false);
