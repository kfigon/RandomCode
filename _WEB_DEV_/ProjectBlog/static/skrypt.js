
function klik() {

    var daneUsera = document.getElementById('daneUsera').value;
    console.log(daneUsera);
}

function wyslijJsona(dane, callback) {
    var xhr = new XMLHttpRequest();

    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            // var json = JSON.parse(xhr.responseText);
            // console.log("zwrotka: "+json.dane);
            callback();
        }
    };

    var data = JSON.stringify(dane);
    xhr.send(data);
}