from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from Config import *
from flask_bcrypt import Bcrypt


app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)

from user_controller import *

@app.route("/", methods = ['GET'])
def index():
    return render_template("index.html")

@app.route("/login", methods = ['GET'])
def login():
    return render_template("login.html")

@app.route("/register", methods = ['GET'])
def register():
    return render_template("register.html")

@app.route("/register", methods = ['POST'])
def createUser():
    existencia = get_user_byname(request)
    matchPass = comp_claves(request)
    #print(existencia)
    errores = []
    if(existencia == True):
        errores.append('El nombre de usuario ya existe')
    if(matchPass == False):
        errores.append('Las contraseñas no coinciden')
    if(len(errores) >= 1):
        print(errores)
        return render_template("register.html", message = errores)
    else:
        res = create_user(request)
        return render_template("login.html", respuesta = res)
    # if(existencia == False):
    # else:
    #     res = {'Error':'El nombre de usuario ya existe'}
    #     return render_template("register.html", message = res)

if __name__ == "__main__":
    app.run()