var submit = document.getElementById("submit");
var insert_txt = document.getElementById("insert");
var new_txt = document.createTextNode("hi");
var submit = document.getElementById("submit");

function validation(){

}
//Sets value of title input equal to title_value
var title_value = document.getElementById("labelTitle").value;

var onClick = function() {
    //saves location values
    var title_value = document.getElementById("labelTitle").value;
    var body_value = document.getElementById("labelComment").value;


    var content = {}
    content.title = title_value;
    content.body = body_value;

    new_post(content);

    insert_txt.textContent = title_value;
};

submit.addEventListener("click", onClick, false);

/*-------------------------------AJAX-------------------------------*/

//Inserts table into webpage
var display_table = function (data) {
    var entries = data.feed.entry
    var insert = document.getElementById("insert");


    for (var i = 0; i < entries.length; i++) {
        var entry = entries[i]

        //catches the title, body, and timestamp within entry
        var title = entry.gsx$posttitle.$t
        var body = entry.gsx$postbody.$t
        var time = entry.gsx$timestamp.$t

        //creates tag elements
        var new_tr = document.createElement("tr");
        var td_time = document.createElement("td");
        var td_title = document.createElement("td");
        var td_body = document.createElement("td");

        //appends text nodes to td tags
        td_time.appendChild(document.createTextNode(time));
        td_title.appendChild(document.createTextNode(title));
        td_body.appendChild(document.createTextNode(body));

        //appends the td tags to tr tag
        new_tr.appendChild(td_time);
        new_tr.appendChild(td_title);
        new_tr.appendChild(td_body);

        //appends the tr tag to insert id location
        insert.appendChild(new_tr);
    }
}

//AJAX get
$.ajax({
    type: 'GET',
    url: "https://spreadsheets.google.com/feeds/list/1ntmcFZk4R0Owmez5eKc0bcu_PftAKwWyXDWTqmypPgI/default/public/values?alt=json-in-script",
    //data: { get_param: 'value' },
    dataType: 'jsonp',
    success: display_table
});

//AJAX post
function new_post(data){
    $.ajax({
        url: "https://docs.google.com/forms/d/1blH7mM6udvlyJ0SrPmbXoNPZg8XCqDQaxHTPrK0HQbA/formResponse",
        data: data,
        type: "POST",
        dataType: "json",
        success: function (data) {
            console.log("Got Response: " + data);
        }
    });
}
