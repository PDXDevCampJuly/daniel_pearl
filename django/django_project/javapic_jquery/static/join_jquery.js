/*--------------------------Validate Input--------------------------*/

function validation(){
    //validates form and returns true or false

        if ($("input[name=name]").val() === ""){
            alert("You must enter a name.");
            return false;
        }
        if ($("input[name=username]").val() === ""){
            alert("You must enter a username.");
            return false;
        }
        if ($("input[name=email]").val() === ""){
            alert("You must enter a email.");
            return false;
        }
        return true;
}
/*----------------------Submit and Change name----------------------*/

$("#signup").submit(function(e){
    //submits the form and returns to the gallery page

    e.preventDefault(); //prevents form from submitting without input

    if (validation()){
        console.log(name);
        sessionStorage.setItem("name_input", $("input[name=name]".value)); //saves name value into a key
        window.location.href = "gallery_jquery.html"; //switches to gallery.html
    }
});
