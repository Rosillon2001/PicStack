datos();

function datos(){
    fetch('/user/data',{
        method: 'GET'
    }).then(response => response.json())
    
    .then(data => {
        console.log('Datos de eliminacion',data);
        // username = data.username;
        id = data.id;
        // console.table(data);
        deleteId(id);

    })
    .catch(error => console.log('ERROR', error));
}

//pasarle el id al boton de eliminar cuenta
function deleteId(id){
    var del = document.getElementById('deleteId')

    del.setAttribute('href', `/deleteUser/${id}`)
}

// funcion para la muestra y oculto de los input password
function hideNshow(input, button, sh1, sh2){
    var show = document.getElementById(sh1)
    var hide = document.getElementById(sh2)
    var btnSH = document.getElementById(button)
    var pass = document.getElementById(input);
    var cont = 0;
    btnSH.onclick = function (){
        switch(cont){
            case 0:
                show.style.display = 'block';
                hide.style.display = 'none';
                pass.setAttribute('type', 'text');
                cont = 1;
                break;
                
            case 1:
                show.style.display = 'none';
                hide.style.display = 'block';
                pass.setAttribute('type', 'password');
                cont = 0;
                break;
        } 
    }
}
hideNshow('passwordProfile1', 'buttonSH1', 'showpassP1', 'hidepassP1');
hideNshow('passwordProfile2', 'buttonSH2', 'showpassP2', 'hidepassP2');