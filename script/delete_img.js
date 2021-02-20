function delete_img(image_url, filter)
{
    if (image_url.length <= 1)
    {
        alert("empty url");
        return;
    }
    // сборка запроса
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    var raw = JSON.stringify({"url": image_url, "type": filter});
    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    // отправка запроса
    fetch(" https://h20vb2nem5.execute-api.us-east-1.amazonaws.com/stage1", requestOptions)
    .then(response => response.text())
    .then(result => { 
        var a = document.createElement('a');
        var data = JSON.parse(result).body;
     
        if (data == 'yes')
        {
            alert('image deleted');
            return;
        }
        else
        {
            alert('nothing to delete');
            return;
        }   
    })
}  

      