from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from Config import *


app = Flask(__name__)
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
    return create_user(request)

if __name__ == "__main__":
    app.run()