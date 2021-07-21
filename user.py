from app import db
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(60), nullable=False, unique=True)
    clave = db.Column(db.String(150), nullable=False)

    def __init__(self, nombre_usuario, clave):
        self.nombre_usuario = nombre_usuario
        self.clave = clave