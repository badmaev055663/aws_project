function select_by_size(min, max)
{
    min_int = Number.parseInt(min);
    max_int = Number.parseInt(max);
    if (min_int >= max_int)
    {
        alert('upper bound is less than lower');
        return;
    }
    if (min_int < 0)
    {
        alert('bounds cannot be negative');
        return;
    }
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
        if (data == 'None')
        {
            alert('such records not found');
            return;
        }
        var rows = data.length;
        document.createElement('table');
      
        document.write('<table>');
        for (var i = 0; i < rows; i++) {
            var url = data[i].url;
            var type = data[i].type;
            var date = data[i].upload_time;
            var size = data[i].size;
            document.write('<tr style="border: 1px solid black;"><td style="border: 1px solid black;">'
                        + url +'</td><td style="border: 1px solid black;">'
                        + type +'</td><td style="border: 1px solid black;">'
                        + date +'</td><td style="border: 1px solid black;">'
                        + size +'</td></tr>');
        }  
        document.write('</table>');  
    })
}  