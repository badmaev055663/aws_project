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
        if (data == 'None')
        {
            alert('such records not found');
            return;
        }
        var rows = data.length;
        document.createElement('table');
        document.write('<table style="border: 2px solid black;">');
        for (var i = 0; i < rows; i++) {
            var url = data[i].url;
            var type = data[i].type;
            var date = data[i].upload_time;
            document.write('<tr style="border: 1px solid black;"><td style="border: 1px solid black;">'+ url +'</td><td style="border: 1px solid black;">'+ type +'</td><td style="border: 1px solid black;">'+ date +'</td></tr>');
        }  
        document.write('</table>');  
    })
}  