from app import db
from repositorio import Repositorio

def create_repo(request):
    # se obtienen los datos del form
    nombre = request.form['nombreRepo']
    idU = request.form['userRepo']

    print(nombre + str(idU))
    message = [] 
    errors = []

    existe = get_repo(request)
    #manejo de errores 
    if (existe == True):
        errors.append('Ya creo un repositorio con este nombre')
        message.append('Ya creo un repositorio con este nombre')
    if len(errors) > 0:
        return message
    else:
        repo = Repositorio(nombre, idU)
        db.session.add(repo)
        db.session.commit()
        message.append('Repositorio creado')
        return message
    

def get_repo(request):
    comparable = ''
    repetido = []
    nombre = request.form['nombreRepo']
    idU = request.form['userRepo']
    existence = db.session.query(Repositorio).filter(Repositorio.id_usuario == idU)
    for row in existence:
        comparable = row.nombre_repo
        print(comparable)
        if comparable == nombre:
            repetido.append(comparable)
    if len(repetido) >= 1:
        return True
    else:
        return False

def get_user_repos(id):
    repos = db.session.query(Repositorio).filter(Repositorio.id_usuario == id)
    repoList = []
    for row in repos:
        repo = {
            'id': row.id_repo,
            'nombre': row.nombre_repo,
            'user': row.id_usuario
        }
        repoList.append(repo)
    return repoList
    # users = User.query.all()
    # user_list=[]
    # for user in users:
    #     user_data = {'id': user.id, 
    #                 'name': user.name, 
    #                 'username': user.username, 
    #                 'email': user.email }
    #     user_list.append(user_data)

    # return {'users': user_list}