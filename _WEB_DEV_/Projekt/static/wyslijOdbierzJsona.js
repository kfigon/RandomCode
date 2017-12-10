function wyslijJsona(url) {

    var xhr = new XMLHttpRequest();

    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var json = JSON.parse(xhr.responseText);
            console.log("zwrotka: "+json.dane);
        }
    };
    var dane = {"x":"dane123", "id":'dane345'};
    console.log("wysylam jsona: x:" + dane.x + ' id:'+dane.id);
    var data = JSON.stringify(dane);
    xhr.send(data);
}