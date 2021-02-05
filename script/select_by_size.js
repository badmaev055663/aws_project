function select_by_size(min, max)
{
    // сборка запроса
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    var raw = JSON.stringify({"min": min, "max": max});
    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    // отправка запроса
    fetch("https://g54xj7ebl8.execute-api.us-east-1.amazonaws.com/stage1", requestOptions)
    .then(response => response.text())
    .then(result => { 
        // отобразить результат  
        var data = JSON.parse(result).body;
        var rows = data.length;
        var table = document.createElement('table');
        
        document.write('<div className="table1"><table className="table">');
        for (var i = 0; i < rows; i++) {
            var url = data[i].url;
            var type = data[i].type;
            var size = data[i].size;
            document.write('<tr className="mess-hide"><td className="url">'+ url +'</td><td className="type">'+ type +'</td><td className="size (KiB)">'+ size + '</td></tr>');
        }  
        document.write('</table></div>');  
    })
}  