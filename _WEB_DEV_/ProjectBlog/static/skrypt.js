function dodajArt() {
    var tytul = document.getElementById('tytul-arta').value;
    var tresc = document.getElementById('tresc-arta').value;

    var obj = {
        tytul: tytul,
        tresc: tresc
    };

    wyslijJsona(obj, 'http://127.0.0.1:5000/newpost', function(status){
        var wynik = document.getElementById('wynik-dodania-arta');

        if(status === 200) {
            wynik.className = "wynik-dodania-arta-ok";
            wynik.innerText = "Udalo sie!";
        } else {
            wynik.className = "wynik-dodania-arta-fail";
            wynik.innerText = "Fail!";
        }
    });
}

function wyslijJsona(dane, url, callback) {
    var xhr = new XMLHttpRequest();

    xhr.open("POST", url, false);
    xhr.setRequestHeader("Content-type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            // var json = JSON.parse(xhr.responseText);
            // console.log("zwrotka: "+json.dane);
            callback(xhr.status);
        }
    };

    var data = JSON.stringify(dane);
    xhr.send(data);
}