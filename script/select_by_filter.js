function select_by_filter(filter)
{
    // сборка запроса
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    var raw = JSON.stringify({ "type": filter });
    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    // отправка запроса
    fetch("https://ecwdkgqtyg.execute-api.us-east-1.amazonaws.com/stage1", requestOptions)
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
            var url = data[i].url;
            var date = data[i].upload_time;
            var size = data[i].size;
            document.write('<tr style="border: 1px solid black;"><td style="border: 1px solid black;">'+ url +'</td><td style="border: 1px solid black;">'+ size +'</td><td style="border: 1px solid black;">'+ date +'</td></tr>');
        }  
        document.write('</table>');  
    })
}  