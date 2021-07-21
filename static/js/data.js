 window.onload = datos;

function datos(){
    fetch('/user/data',{
        method: 'GET'
    }).then(response => response.json())
    
    .then(data => {
        console.log('Datos del usuario',data);
        username = data.username;
        id = data.id;
        console.table(data);
        showNav(username, id);

    })
    .catch(error => console.log('ERROR', error));
}

function showNav(username,id){
    var user = document.getElementById('navUsername') // <div> del username
    var userid = document.getElementById('userid') //<a> etiqueta 

    userid.setAttribute('href', `/user/${id}`)
    user.innerHTML = `${username}`;
}