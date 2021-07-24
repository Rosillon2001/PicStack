from flask import Flask, request, render_template, session, redirect, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from Config import *
import os
import errno

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, './templates')
app = Flask(__name__, template_folder=template_path)
app.config.from_object(ProductionConfig)
db = SQLAlchemy(app)

# ruta de guardado de imagenes
UPLOAD_FOLDER = os.path.abspath('./static/uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
try:
    os.mkdir('./static/uploads')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
from user_controller import *


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
        global IdU
        IdU = get_user_id(user)
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
        return render_template('login.html', message = errores), 300
    else:
        session['username'] = username
        # global message
        # message = session['username']
        Userid = get_user_id(session['username'])
        session['id'] = Userid
        # global sendId 
        # sendId = session['id']

        return redirect("/home")

# ------------------------------------------------------- Manejo de usuarios --------------------------------------------------

@app.route('/user/data', methods = ['GET'])
def sendData():
    username = ''
    idu = 0
    while username == '' or idu == 0:
        try:
            username = session['username']
            idu = session['id']
        except:
            print()
    print (username, idu)
    return {'username':username, 'id':idu}

@app.route('/home', methods = ['GET'])
def feed():
    return render_template('home.html')

@app.route('/images', methods = ['GET'])
def repo():
    idu = 0
    while idu == 0:
        try:
            idu = session['id']
        except:
            print()
    repositorios = get_user_repos(idu)
    # print(repositorios[0]['nombre'])
    return render_template('images.html', repositorios = repositorios)

@app.route('/user/<id>', methods =['GET'])
def showdata(id): 
    datos = get_user_byid(id)
    print(datos)
    return render_template('profile.html', datos = datos)

@app.route('/updateUser', methods = ['POST'])
def updateUser():
    username = ''
    id = 0
    while username == '':
        try:
            username = session['username']
            id = session['id']
        except:
            username = ''
    update = updateData(request, username, id)
    print (update)

    if update != None:
        datos = get_user_byid(id)
        return render_template('profile.html', errores = update, datos = datos)
    else:    
        while 'username' in session or 'id' in session:
            try:
                session.pop('username')
                session.pop('id')
            except:
                print('Cerrando la sesion')
        return  redirect('/login')

@app.route('/logout', methods =['GET'])
def logout(): 
    session.pop('username')
    session.pop('id')
    return  redirect('/login')

@app.route('/deleteUser/<id>', methods = ['GET'])
def deleteUser(id):
    response = user_delete(id)
    print(response)
    return redirect('/')

# ---------------------------------------------------Manejo de repositorios--------------------------------------------------------------
from repo_controller import *

@app.route('/createRepo', methods = ['POST'])
def newRepo():
    repo = create_repo(request)
    success= []
    error = []
    if repo[0] == 'Repositorio creado':
        success.append('Repositorio creado')
        return redirect('/images')
    if repo[0] == 'Ya creo un repositorio con este nombre':
        error.append('Ya creo un repositorio con este nombre')
        return render_template('/images.html', error = error)

@app.route('/editRepo/<id>', methods = ['POST'])
def editRepo(id):
    infor = edit_repo(request, id)
    error = []
    if infor is None:
        return redirect('/images')
    else:
        return render_template('/images.html', infor = infor)
    
@app.route('/deleteRepo/<id>', methods = ['GET'])
def deleteRepo(id):
    delete_repo(id)
    return redirect('/images')

# -----------------------------------------------------Manejo de imagenes------------------------------------------------------------

from imagen_controller import * 

@app.route('/repoImage/<id>', methods = ['GET'])
def imagesRepo(id):
    idRepo = id
    nombreImg = []
    username = ''
    repoName = get_repo_name(id)
    imagenesRepo = repo_images(id)
    
    for i in range (0,len(imagenesRepo)):
        nombreImg.append(imagenesRepo[i]['ruta'])

    while username == '':
        try:
            username = session['username']
        except:
            username = ''
    return render_template('imageRepo.html', idRepo = idRepo, autor = username, repoName = repoName, imagenes = imagenesRepo)

@app.route('/image/upload/<id>', methods = ['POST'])#este id es el id del repositorio al cual se sube
def postImage(id):
    datos = create_image(request)
    print (datos) # esquema del arreglo datos -> datos[0] = FileStorage:archivo ; datos[1] = nombre/titulo ;
                    #datos[2] = autor ; datos[3] = tags ; 
    # obtencion de la imagen
    # tags = datos[3].split('#')
    # del tags[0]
    print (datos[3])
    f = datos[0]
    filename = f.filename
    # print(filename)
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    # print('retorno de data')
    # print(imag_data(1))

    ruta = '/repoImage/' + str(id)
    return redirect(ruta)

# --------------------------------------------------- Inicializacion del server -------------------------------------------------------
if __name__ == "__main__":
    app.run()
    