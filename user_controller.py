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

