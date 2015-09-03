
/*--------------------------Validate Input--------------------------*/

function validation(){
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

function submit_form(){
    //submits the form and returns to the gallery page

    $("#signup").submit(function(e){
        e.preventDefault();

        if (validation()){
            console.log(validation());
            change_name();
            window.location.href = "gallery_jquery.html";
        }
    });
}

function change_name(){
    //Creates sessions storage

    sessionStorage.setItem("name_input", $["inpupt[name=name].val()"]);
}
 
submit_form();
