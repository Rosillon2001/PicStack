datos();

function datos(){
    fetch('/user/data',{
        method: 'GET'
    }).then(response => response.json())
    
    .then(data => {
        id = data.id;
        console.log('Id del usuario', id);
        // console.table(data);
        user_repo(id);

    })
    .catch(error => console.log('ERROR', error));
}

function user_repo(id){
    var iduser = document.getElementById('userRepo');

    iduser.setAttribute('value',`${id}`)
}