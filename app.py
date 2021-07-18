from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from src.Config import *
from src.user_controller import *

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")