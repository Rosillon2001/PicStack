function navs(){
    var home = document.getElementById('homeNav');
    var repo = document.getElementById('repoNav');

    home.onclick = function (){
        home.classList.add('active')
        repo.classList.remove('active')
    }
    repo.onclick = function (){
        home.classList.remove('active')
        repo.classList.add('active')
    }
}

navs()