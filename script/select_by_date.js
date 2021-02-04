function select_by_date(count)
{
    // сборка запроса
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    var raw = JSON.stringify({"count": count});
    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    // отправка запроса
    fetch("https://1u9wwe0mb4.execute-api.us-east-1.amazonaws.com/stage1", requestOptions)
    .then(response => response.text())
    .then(result => { 
        // отобразить результат  
        var data = JSON.parse(result).body;
        var rows = data.length;
        var table = document.createElement('table');
        
        document.write('<div className="table1"><table className="table">');
        for (var i = 0; i < rows; i++) {
            var url = data[i].url;
            var date = data[i].upload_time;
            var type = data[i].type;
            document.write('<tr className="mess-hide"><td className="url">'+ url +'</td><td className="date">'+ date +'</td><td className="type">'+ type +'</td></tr>');
        }  
        document.write('</table></div>');  
    })
}  