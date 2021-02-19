function search_by_url(url)
{
    if (url.length <= 1)
    {
        alert("empty url");
        return;
    }
    // сборка запроса
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    var raw = JSON.stringify({ "url": url });
    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    // отправка запроса
    fetch("https://k1c5dq3uzk.execute-api.us-east-1.amazonaws.com/stage1", requestOptions)
    .then(response => response.text())
    .then(result => { 
        // отобразить результат  
        var data = JSON.parse(result).body;
        if (data == 'None')
        {
            alert('not found');
            return;
        }
        var rows = data.length;
        document.createElement('table');
        document.write('<table>');
        for (var i = 0; i < rows; i++) {
            var type = data[i].type;
            var date = data[i].upload_time;
            var size = data[i].size;
            document.write('<tr style="border: 1px solid black;"><td style="border: 1px solid black;">'
                        + type +'</td><td style="border: 1px solid black;">'
                        + size +'</td><td style="border: 1px solid black;">'
                        + date +'</td></tr>');
        }  
        document.write('</table>');  
    })
}  