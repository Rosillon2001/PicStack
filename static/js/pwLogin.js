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
hideNshow('passwordLogin1', 'buttonL1', 'showpassL1', 'hidepassL1');
