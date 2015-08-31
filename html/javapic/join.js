/*-------------------------Create variables-------------------------*/

var name = document.getElementsByName("name");
var username = document.getElementsByName("username");
var email = document.getElementsByName("email");
var submit = document.getElementById("submit");
var signup = document.getElementById("signup");

/*-------------------------Catch user input-------------------------*/

var name_input = document.querySelector("input[name=name]");
var username_input = document.querySelector("input[name=username]");
var email_input = document.querySelector("input[name=email]");

/*--------------------------Validate Input--------------------------*/

function validation(){
    //validates the information that has been filled in
    if (name_input.value === "") { // validates name entered
        alert("You must enter a name.");
        return false;
    }
    if (username_input.value === "") { //validates userName entered
        alert("You must enter a username.");
        return false;
    }
    if (email_input.value === "") { //validates email entered
        alert("You must enter an email.");
        return false;
    }
    return true; //returns true when all has been filled in
}

/*----------------------Submit and Change name----------------------*/

function submit_form(e){
    //submits the form and returns to the gallery page

    e.preventDefault();
    if (validation()){
        change_name();
        console.log(change_name());

        document.location.href = "gallery.html";
    }
}

function change_name(){
    //Creates sessions storag
    sessionStorage.setItem("name_input", name_input.value);
}
 

/*-----------------------Add Event Listeners-----------------------*/

signup.addEventListener("submit", submit_form, false);
