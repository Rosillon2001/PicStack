from flask import Flask, request, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect
from Config import *
import os

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, './templates')
app = Flask(__name__, template_folder=template_path)
app.config.from_object(ProductionConfig)
db = SQLAlchemy(app)

from user_controller import *

message = ''
sendId = 0

@app.before_request
def session_management():
  session.permanent = True


@app.route("/", methods = ['GET'])
def index():
    return render_template("welcome.html")

@app.route("/login", methods = ['GET'])
def login():
    return render_template("login.html")

@app.route("/register", methods = ['GET'])
def register():
    return render_template("register.html")

@app.route("/register", methods = ['POST'])
def createUser():
    user = request.form['usernameRegister']
    existencia = get_user_byname(user)
    matchPass = comp_claves(request)
    #print(existencia)
    errores = []
    if(existencia == True):
        errores.append('El nombre de usuario ya existe')
    if(matchPass == False):
        errores.append('Las contraseñas no coinciden')
    if(len(errores) >= 1):
        #print(errores)
        return render_template("register.html", message = errores)
    else:
        res = create_user(request)
        return render_template("login.html", respuesta = res)
    # if(existencia == False):
    # else:
    #     res = {'Error':'El nombre de usuario ya existe'}
    #     return render_template("register.html", message = res)

@app.route("/login", methods = ['POST'])
def loginUser():
    errores = []
    password = request.form['passwordLogin']
    username = request.form['usernameLogin']
    print(password)

    if not password:
        errores.append('Ingrese la contraseña')
    
    elif not username:
        errores.append('Ingrese el nombre de usuario')

    else:
        existencia = get_user_byname(username)

        if existencia == False:
            errores.append('El usuario no está registrado')
        else: 
            verif = auth_pass(username, password)
            if verif == False:
                errores.append('La contraseña es incorrecta')

    if(len(errores) >= 1):
        return render_template('login.html', message = errores)
    else:
        session.permanent = True
        session['username'] = username
        global message
        message = session['username']
        Userid = get_user_id(session['username'])
        session['id'] = Userid
        global sendId 
        sendId = session['id']

        return redirect("/home")

@app.route('/user/data', methods = ['GET'])
def sendData():
    username = session['username']
    id = session['id']
    print (username, id)
    return {'username':username, 'id':id}

@app.route('/home', methods = ['GET'])
def feed():
    return render_template('home.html')

@app.route('/images', methods = ['GET'])
def repo():
    return render_template('images.html')

@app.route('/user/<id>', methods =['GET'])
def showdata(id): 
    datos = get_user_byid(id)
    print(datos)
    return render_template('profile.html', datos = datos)

# @app.route('/updateUser/<id>', methods = ['PUT'])
# def updateUser(id):
#     return    


if __name__ == "__main__":
    app.run()
    