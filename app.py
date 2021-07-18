from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from src.Config import *
from src.user_controller import *

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)

@app.route("/")
def index():
    return "Elpepe"