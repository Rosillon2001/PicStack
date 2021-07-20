from app import db
from user import User
import bcrypt

def create_user(request):
    username = request.form['username']
    password = request.form['password']
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

def get_user_byname(request):
    comparable = '';
    user = request.form['username']
    existence = db.session.query(User).filter(User.nombre_usuario == user)
    for row in existence:
        print('En la db ->')
        print(row.nombre_usuario)
        comparable = row.nombre_usuario
    if user == comparable:
        return True
    return False

def get_user_pass(request):
    user = request.form['username']
    datos = db.session.query(User).filter(User.nombre_usuario == user)
    for row in datos:
        print('En la db ->')
        print(row.clave)
    return row.clave

def auth_pass(request, password):
    claveDB = get_user_pass(request).encode('utf-8')
    print(claveDB)
    verif = bcrypt.checkpw(password.encode('utf-8'), claveDB)
    if verif == True:
        return True
    else:
        return False

def comp_claves(request):
    clave = request.form['password']
    conf = request.form['passwordConfirm']
    if (clave == conf):
        return True
    else:
        return False

