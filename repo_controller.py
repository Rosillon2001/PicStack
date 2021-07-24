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

def get_repo_name(id):
    nombreRepo = []
    query = db.session.query(Repositorio).filter(Repositorio.id_repo == id)
    for row in query:
        nombreRepo.append(row.nombre_repo)
    return nombreRepo

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


def edit_repo(request, id):
    comparable = ''
    repetido = []
    mensaje = ['Ya tiene un repositorio con ese nombre']
    editar = False
    repo = Repositorio.query.get(id)
    nuevoNombre = request.form['nuevoNombreRepo']
    idnewuser = request.form['userNewRepo']
    existence = db.session.query(Repositorio).filter(Repositorio.id_usuario == idnewuser)
    for row in existence:
        comparable = row.nombre_repo
        print(comparable)
        if comparable == nuevoNombre:
            repetido.append(comparable)
    if len(repetido) >= 1:
        editar = False
    else:
        editar = True

    if editar == True:
        repo.nombre_repo = nuevoNombre
        db.session.commit()
    else: 
        return mensaje

def delete_repo(id):
    repo = Repositorio.query.get(id)
    db.session.delete(repo)
    db.session.commit()
    return {'Info':'Repositorio eliminado'}


    # users = User.query.all()
    # user_list=[]
    # for user in users:
    #     user_data = {'id': user.id, 
    #                 'name': user.name, 
    #                 'username': user.username, 
    #                 'email': user.email }
    #     user_list.append(user_data)

    # return {'users': user_list}