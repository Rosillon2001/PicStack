from app import db
from user import User
from app import bcrypt

def create_user(request):
    username = request.form['username']
    password = request.form['password']
    hashPass = bcrypt.generate_password_hash(password)
    print('pass: '+str(password)+' hash: '+str(hashPass))
    #user = User(username,)
    #db.session.add(user)
    #db.session.commit()
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

def comp_claves(request):
    clave = request.form['password']
    conf = request.form['passwordConfirm']
    if (clave == conf):
        return True
    else:
        return False