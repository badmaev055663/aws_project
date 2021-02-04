function img_process(image_url, filter)
{
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
    fetch("https://8zkgi8tu20.execute-api.us-east-1.amazonaws.com/stage1", requestOptions)
    .then(response => response.text())
    .then(result => { 
        // скачивание картинки   
        var a = document.createElement('a');
        a.href = JSON.parse(result).body;
        a.setAttribute("download", a.href.slice(-11));
        a.click();   
    })
}  

      