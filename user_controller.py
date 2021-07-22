from abc import abstractproperty
from app import db
from user import User
import bcrypt

def create_user(request):
    username = request.form['usernameRegister']
    password = request.form['passwordRegister1']
    salt = bcrypt.gensalt()
    hashPass = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
    print('pass: '+str(password)+' hash: '+str(hashPass))

    
    user = User(username, hashPass)
    db.session.add(user)
    db.session.commit()
    return {'message': 'user created'}

def get_user_byid(id):
    user = User.query.get(id)
    if user is None:
        return {'error': 'user not found'}
    return {'id_usuario': user.id_usuario , 
            'nombre_usuario': user.nombre_usuario, 
            'clave':user.clave}

def get_user_byname(user):
    comparable = '';
    existence = db.session.query(User).filter(User.nombre_usuario == user)
    for row in existence:
        print('En la db ->')
        print(row.nombre_usuario)
        comparable = row.nombre_usuario
    if user == comparable:
        return True
    return False

def get_user_pass(user):
    datos = db.session.query(User).filter(User.nombre_usuario == user)
    for row in datos:
        clave = row.clave
    return clave

def get_user_id(username):
    datos = db.session.query(User).filter(User.nombre_usuario == username)
    for row in datos:
        user = row.id_usuario
    return user

def updateData(request, username, id):
    user = User.query.get(id)
    newUsername = request.form['username']
    passActual = request.form['passwordProfile1']
    passNueva = request.form['passwordProfile2']
    newpass = False

    errores = []

    if passNueva != '':
        newpass = True
    if passActual == '' or username == '' :
        errores.append('No deje campos vacíos')

    else:
        if auth_pass(username, passActual) == False:
            errores.append('La contraseña actual no coincide con la registrada')

        if passActual == passNueva and auth_pass(username, passActual) == True:
            errores.append('La constraseña es la misma, ingrese una nueva')

    if len(errores) < 1:
        user.nombre_usuario = newUsername
        if newpass == True:
            user.clave = hashing(passNueva)
        db.session.commit()
    else: 
        return errores

def user_delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return {'message': 'user deleted'}

# -------------------------------------------------comparacion y autenticacion de contraseñas-------------------------------------------
def auth_pass(user, password):
    claveDB = get_user_pass(user).encode('utf-8')
    print(claveDB)
    verif = bcrypt.checkpw(password.encode('utf-8'), claveDB)
    if verif == True:
        return True
    else:
        return False

def comp_claves(request):
    clave = request.form['passwordRegister1']
    conf = request.form['passwordRegister2']
    if (clave == conf):
        return True
    else:
        return False

def hashing(password):
    salt = bcrypt.gensalt()
    hashPass = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
    
    return hashPass