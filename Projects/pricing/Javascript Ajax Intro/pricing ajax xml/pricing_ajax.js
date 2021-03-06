/* ----------------------------XML AJAX-----------------------------*/


// $(.ajax)({ //Load the xml file using ajax
//     type: "GET",
//     url: "data/stock.xml",
//     dataType: "xml",
//     success:function(xml){
//
//         var stock = $.parseXML(xml),
//             $xml = $(stock);
//         $xml.find("")
//     }
// });

/* ------------------------Assign Variables-------------------------*/

var inventory = document.getElementById("inventory");
var woodStock = document.getElementById('woodStock');
var woodStock, material, price;

/* ---------------------Create Product Object-----------------------*/

function Product(name, stock, price) {
    this.checked = false;
    this.name = name;
    this.stock = stock;
    this.price = price;

    this.adjustStock = function(num) {
        this.stock -= num;
    };
    this.inStock = function() {
        return this.stock > 0;
    };
}
var materials = [];

populateInventory();

/* ------------------Populate Inventory in HTML--------------------*/

function populateInventory(){
    //Loop through materials
    //Add a row for each item in materials
    //Make sure that stock class reflects inStock
    //Make sure that checkbox status reflects checked
    for (var i = 0; i < materials.length; i++){
        var newProdRow = document.createElement('tr');
        var checkboxCell = document.createElement('td');
        var checkbox = document.createElement('input');
        checkbox.type = "checkbox";
        checkbox.checked = materials[i].checked;
        checkboxCell.appendChild(checkbox);
        newProdRow.appendChild(checkboxCell);

        //Name Column
        var nameCol = document.createElement('td');
        var nameText = document.createTextNode(materials[i].name);
        nameCol.appendChild(nameText);
        newProdRow.appendChild(nameCol);

        //Price Column
        var priceCol = document.createElement('td');
        var priceText = document.createTextNode('$' + materials[i].price);
        priceCol.appendChild(priceText);
        newProdRow.appendChild(priceCol);

        //Stock
        var stockCol = document.createElement('td');
        stockCol.className = materials[i].inStock();
        var stockText = document.createTextNode(materials[i].stock);
        stockCol.appendChild(stockText);
        newProdRow.appendChild(stockCol);

        inventory.appendChild(newProdRow);
    }
}

/* ---------------------Checkbox functions-----------------------*/

function checkAll(checkbox) {
    if (checkbox.checked) {
        var inputs = inventory.getElementsByTagName('input')
        for (var i = 0; i < inputs.length; i++) {
            if (inputs[i].type == "checkbox") {
                inputs[i].checked = checkbox.checked;
            }
        }
    }
    if (checkbox.checked == false) {
        var inputs = inventory.getElementsByTagName('input')
        for (var i = 0; i < inputs.length; i++) {
            if (inputs[i].type == "checkbox") {
                inputs[i].checked = false;
            }
        }
    }
}

function removeStock() {
    var rows = inventory.getElementsByTagName('tr');

    for (var i = 0; i < rows.length; i++) {
        var inputs = rows[i].getElementsByTagName('input');
        if (inputs[0].type == "checkbox") {
            if (inputs[0].checked) {
                //Flip the status of the stock column
                var stock = rows[i].lastElementChild;
                stock.className = 'false';
                stock.textContent = 'No';
            }
        }
    }
}

function addStock() {
    var rows = inventory.getElementsByTagName('tr');

    for (var i = 0; i < rows.length; i++) {
        var inputs = rows[i].getElementsByTagName('input');
        if (inputs[0].type == "checkbox") {
            if (inputs[0].checked) {
                //Flip the status of the stock column
                var stock = rows[i].lastElementChild;
                stock.className = 'true';
                stock.textContent = 'Yes';
            }
        }
    }
}

function addNewStock() {
    material = document.getElementById('material').value;
    price = document.getElementById('price').value;

    document.querySelectorAll('tr')

    if (material != "" && price != "" && isNaN(price) == false) {
        var newRow = "<tr>";
        newRow += '<td><input type="checkbox"/></td>';
        newRow += '<td>' + material + '</td>';
        newRow += '<td>$' + price + '</td>';
        newRow += '<td class="true"> 10 </td>';
        newRow += '</tr>';

        inventory.innerHTML += newRow

        document.getElementById('material').value = '';
        document.getElementById('price').value = '';
    }
}

/* --------------------------AJAX request--------------------------*/

var newRequest = new XMLHttpRequest(); //Create XMLHttp Request Object

newRequest.onload = function(){
    if(newRequest.status === 200){
        //console.log(newRequest.responseXML);
        var response = newRequest.responseXML;
        var items = response.getElementsByTagName("item");
        //console.log(items);
        for(var i=0; i<items.length; i++){
            var product = new Product(
                items[i].getAttribute("name"),
                items[i].getAttribute("price"),
                items[i].getElementsByTagName("numInStock")[0].textContent);
            materials.push(product);

            // console.log(items[i].getAttribute("price"));
            // console.log(items[i].getAttribute("name"));
            // console.log(items[i].getElementsByTagName('numInStock')[0].textContent);
        }
        populateInventory();
    }
};
